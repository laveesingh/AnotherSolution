$(document).ready(function(){
  $("#plot").click(function(){
    $.ajax({
      url: '/swoosh/plot/',
      dataTye: 'json',
      success: function(data){
        $("#imagediv").html(data);
      }
    });
  });
});
