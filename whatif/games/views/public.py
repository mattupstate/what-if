from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson 
from whatif.games.documents import Game, GameInstance, Question, Response


class TokenAverage(object):
    token = None
    width = 0
    
    def __init__(self, token, width):
        self.token = token
        self.width = width

def _template(name):
    return 'games/%s.html' % name

def _get_game_or_404(game_id):
    try:
        return Game.objects.with_id(game_id)
    except:
        raise Http404

def _respond(template, context, request):
    return render_to_response(_template(template), context, context_instance=RequestContext(request))

def home(request):
    return _respond('index', { "games": Game.objects, }, request)

def play_game(request, game_id):
    game = _get_game_or_404(game_id)
    instance = GameInstance(game=game)
    instance.save()
    return _respond('play', { "instance":instance }, request)
       
def view_game(request, game_id):
    game = _get_game_or_404(game_id)
    token_averages = []
    for token in game.tokens:
        token_averages.append(TokenAverage(token, 0))
        
    instances = GameInstance.objects(game=game)
    total = 0
    for instance in instances:
        if instance.is_complete():
            total += 1
            for response in instance.responses:
                for modifier in response.question.token_modifiers:
                    delta = modifier.yes_modifier if response.response == 1 else modifier.no_modifier
                    for average in token_averages:
                        if average.token == modifier.token:
                            average.width += (delta * 5)
                
    for average in token_averages:
        average.width /= total
            
    return _respond('view', { "game":game, "total":total, "averages":token_averages }, request)

def answer_question(request, instance_id):
    try:
        instance = GameInstance.objects.with_id(instance_id)
        if not instance.is_complete():
            question = Question.objects.with_id(request.POST.get('question_id')) 
            response = Response(question=question, response=int(request.POST.get('response_value')))
            instance.responses.append(response)
            instance.save()
        return HttpResponse(simplejson.dumps({}), mimetype='application/json')
    except:
        return HttpResponse(simplejson.dumps({}), mimetype='application/json')
    
    