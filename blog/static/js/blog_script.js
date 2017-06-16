$(document).ready(function(){
    console.log("The script is running");
    $(".content-markdown").each(function(){
        var content = $(this).text().trim();
        // console.log("content: " + content)
        var marked_content = marked(content);
        // console.log(marked_content);
        $(this).html(marked_content);
    })

    $(".delete-span").on("click", function(){
        var id = $(this).attr('id');
        var this_span = this;
        $.ajax({
            url: "/blog/delete/" + id,
            success: function(data){
                var cur_div = $(this_span).closest('.post-div');
                cur_div.html(data['message']);
                setTimeout(function(){ cur_div.remove(); }, 3000);
                // console.log($(this_span).closest('.post-div').html(data['message']));
            }
        });
    })
})