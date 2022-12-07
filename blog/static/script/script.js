$(document).ready(function(){

  $('.post-image').each(function(){
  
  if($(this).height() > $(this).width() && $(this).height() > 100){
  $(this).css('height', '400px');
  }
  else {
    $(this).css('width', '100%')
  }
  });
  });