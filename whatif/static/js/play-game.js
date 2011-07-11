var instanceId;
var csrfToken;
var questionIndex = -1;
var currentQuestion;
var questions;
var widthMod = 5;

function updateTokens(questionId, response) {
  for(var i = 0; i < gameData.questions.length; i++) {
    var value = gameData.questions[i];
    if(value.id == questionId) {
      var q = value;
      break;
    }
  }
  if(q) {
    $.each(q.token_modifiers, function(index, modifier) {
      var token = modifier.token;
      var mod = (response == 1) ? modifier.yes_modifier : modifier.no_modifier;
      var vehicle = $('#' + token.id);
      vehicle.width(Math.max(0, vehicle.width() + mod * widthMod));
    });
  }
}

function nextQuestion() {
  questionIndex++
  if(questionIndex < questions.length) {
    gotoQuestion(questionIndex);
  } else {
    gotoQuestion(-1);
  }
}

function gotoQuestion(index) {
  if(currentQuestion) {
    currentQuestion.toggle();
  }
  currentQuestion = $(questions[index]);
  currentQuestion.fadeToggle();
}

$(document).ready(function(){
  instanceId = $('#instance-id').text();
  csrfToken = $('#csrf-token').text();
  questions = $('#game-questions').children();
  
  $('.positive').data({response:1});
  $('.negative').data({response:0});
  
  $('.answer-button').click(function(event){
    var questionId = $(this).parent().attr('id');
    var responseValue = $(this).data().response;
    var data = {  
      question_id:questionId, 
      response_value:responseValue, 
      csrfmiddlewaretoken:csrfToken 
    };
    $.post(
      '/instance/' + instanceId + '/respond/', 
      data, 
      function(data) {
        updateTokens(questionId, responseValue);
        nextQuestion();
      }, 
      'json');
  });
  
  nextQuestion();
});
