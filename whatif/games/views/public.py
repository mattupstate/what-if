from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson 
from whatif.games.documents import Game, GameInstance, Question, Response

# Util class for managing token averages
class TokenAverage(object):
    token = None
    width = 0
    
    def __init__(self, token, width):
        self.token = token
        self.width = width

# encapsulated template referrence
def _template(name):
    return 'games/%s.html' % name

# util method for retrieving a game and raising a 404 if its not found
def _get_game_or_404(game_id):
    try:
        return Game.objects.with_id(game_id)
    except:
        raise Http404

# util method for easy http responses
def _respond(template, context, request):
    return render_to_response(_template(template), context, context_instance=RequestContext(request))

# Home page
def home(request):
    return _respond('index', { "games": Game.objects, }, request)

# Start a game
def play_game(request, game_id):
    game = _get_game_or_404(game_id)
    instance = GameInstance(game=game) # Create a new game instance every time
    instance.save()
    return _respond('play', { "instance":instance }, request)
       
# View the cummulative data of a game
def view_game(request, game_id):
    game = _get_game_or_404(game_id)
    token_averages = [] # a list of token averages
    for token in game.tokens:
        token_averages.append(TokenAverage(token, 0))
        
    instances = GameInstance.objects(game=game) # get all instances for the specified game
    total = 0 # total is only for finished games
    
    # This looks ugly, needs refactoring at some point if possible
    # but this basically adds up all the modifiers from completed
    # games so it can be divided by the total afterwards
    for instance in instances:
        if instance.is_complete():
            total += 1
            for response in instance.responses:
                for modifier in response.question.token_modifiers:
                    delta = modifier.yes_modifier if response.response == 1 else modifier.no_modifier
                    for average in token_averages:
                        if average.token == modifier.token:
                            average.width += (delta * 5)
                
    # average division on all tokens
    for average in token_averages:
        average.width /= total
            
    return _respond('view', { "game":game, "total":total, "averages":token_averages }, request)

# Ajax method for answering questions. This isn't the strongest method at the moment since
# is doesn't return any validation messagew
def answer_question(request, instance_id):
    try:
        instance = GameInstance.objects.with_id(instance_id)
        
        # Prevent additional answers if the game is complete
        if not instance.is_complete():
            question = Question.objects.with_id(request.POST.get('question_id')) 
            response = Response(question=question, response=int(request.POST.get('response_value')))
            instance.responses.append(response)
            instance.save()
    except:
        pass
    return HttpResponse(simplejson.dumps({}), mimetype='application/json')
    
    