$(document).ready( function() {
  $( "#new-game-dialog" ).dialog({
    autoOpen: false,
    width: 200,
    height: 165,
    modal: true
  });
  $('.new-game-btn').click( function() {
    $( "#new-game-dialog" ).dialog( "open" );
    return false;
  });  
});