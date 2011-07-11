var instanceId; // Game instance ID
var csrfToken; // CSRF token for when submitting ia ajax
var questionIndex = -1; // Current question index
var currentQuestion; // Current question node
var questions; // All question nodes
var widthMod = 5; // Modifier for vehicle width can be used to give the token bars the appearance of more movement

// Update the token bars based on the answer given to the question
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

// Go to the next question
function nextQuestion() {
  questionIndex++
  if(questionIndex < questions.length) {
    gotoQuestion(questionIndex);
  } else {
    gotoQuestion(-1);
  }
}

// Go to the specified question index
function gotoQuestion(index) {
  if(currentQuestion) {
    currentQuestion.toggle();
  }
  currentQuestion = $(questions[index]);
  currentQuestion.fadeToggle();
}


$(document).ready(function(){
  // Get some values form the HTML
  instanceId = $('#instance-id').text();
  csrfToken = $('#csrf-token').text();
  questions = $('#game-questions').children();
  
  // Set positive buttons with a response value of 1 (YES)
  $('.positive').data({response:1});
  // Set negative buttons with a response value of 0 (NO)
  $('.negative').data({response:0});
  
  // Set all answer buttons to POST to the respond endpoint and go to the next question after a response
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
  
  // Go to the first question
  nextQuestion();
});
