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

    // $(".content-markdown").each(function(){
    //     var content = $(this).text().trim();
    //     var marked_content = marked(content);
    //     $(this).html(marked_content);
    // })

    $(".delete-span").on("click", function(){
        // var confirmed = confirm("Are you sure you want to delete this post?");
        // if (!confirmed)
            // return;
        var id = $(this).attr('id');
        var this_span = this;
        $.ajax({
            url: "/blog/delete/" + id,
            success: function(data){
                var cur_div = $(this_span).closest('.post-div');
                var msg_div = $("#post-list-header");
                if(data['status'] === 'deleted'){
                    setTimeout(function(){ cur_div.fadeOut(3000); }, 1000);
                    msg_div.html(data['message'] + msg_div.html());
                }else{
                    msg_div.html(data['message'] + msg_div.html());
                }
                // console.log($(this_span).closest('.post-div').html(data['message']));
            }
        });
    })

    function loadScriptSync(src, id){
        var s = document.createElement('script');
        s.src = src;
        s.type = 'text/javascript';
        s.async = false;
        document.getElementById(id).appendChild(s);
    }

})