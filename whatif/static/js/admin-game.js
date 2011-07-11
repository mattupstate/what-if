$(document).ready(function(){
  $('#token-text').focusin(function(event){
    $(this).val('');
  }).focusout(function(event){
    var label = 'Add a token...';
    if($(this).val() == '') {
      $(this).val(label);
    }
  });
  
  $('#question-text').focusin(function(event){
    $(this).val('');
  }).focusout(function(event){
    var label = 'Add a question...';
    if($(this).val() == '') {
      $(this).val(label);
    }
  });
  $('.modifier-select').change(function(event){
    $(this).parent().submit();
  })
});
