$(document).ready(function(){

    $("#id_body").on('keyup', function(){
        var body = $(this).val();
        $("#post_preview").html(body);
    })

})