$(document).ready( function() {
  
  // Setup the 'New Game' dialog form
  $( "#new-game-dialog" ).dialog({
    autoOpen: false,
    width: 200,
    height: 165,
    modal: true
  });
  
  // Configure the 'New Game' nav button to open a JQuery dialog
  $('.new-game-btn').click( function() {
    $( "#new-game-dialog" ).dialog( "open" );
    return false;
  });
    
});