$(document).ready(function(){

    /* Following Feature is for altering activated tab in navbar 
    BASE_URL = "http://localhost:8000"
    $(".nav-pill a").each(function(){
        console.log($(this).attr('href'));
        console.log(window.location.href);
        if(BASE_URL + $(this).attr('href') == window.location.href){
            $(this).parent().attr('class', 'nav-pill active');
        }else{
            $(this).parent().attr('class', 'nav-pill');
        }
    })
    */

    $(".content-markdown").each(function(){
        var content = $(this).text().trim();
        var marked_content = marked(content);
        $(this).html(marked_content);
    })

    $(".delete-span").on("click", function(){
        alert("You're not auhorized to delete this post!");
        return;
        var confirmed = confirm("Are you sure you want to delete this post?");
        if (!confirmed)
            return;
        var id = $(this).attr('id');
        var this_span = this;
        $.ajax({
            url: "/blog/delete/" + id,
            success: function(data){
                var cur_div = $(this_span).closest('.post-div');
                cur_div.html(data['message']);
                setTimeout(function(){ cur_div.fadeOut(3000); }, 1000);
                // console.log($(this_span).closest('.post-div').html(data['message']));
            }
        });
    })
})