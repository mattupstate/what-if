$(document).ready(function(){
  
  // Setup the 'Add Token' input field with default text
  $('#token-text').focusin(function(event){
    $(this).val('');
  }).focusout(function(event){
    var label = 'Add a token...';
    if($(this).val() == '') {
      $(this).val(label);
    }
  });
  
  // Setup the 'Add Question' input field with default text
  $('#question-text').focusin(function(event){
    $(this).val('');
  }).focusout(function(event){
    var label = 'Add a question...';
    if($(this).val() == '') {
      $(this).val(label);
    }
  });
  
  // Setup the token modifier drop downs to submit automatically
  $('.modifier-select').change(function(event){
    $(this).parent().submit();
  })
});
