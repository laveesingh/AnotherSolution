$(document).ready(function(){
    console.log("The script is running");

    // $("#plot").on('click', function(){
    //     $.ajax({
    //         url: '/swoosh/plot/',
    //         dataType: 'json',
    //         success: function(data){
    //             $("#imagediv").html(data);
    //         }
    //     });
    // });

    $("#plot").on("click", function(){
        console.log("The plot is clicked");
        if($(this).hasClass("plotted")){
            $(this).removeClass("plotted");
            $("#imagediv").html("");
        }
        else{
            $(this).addClass("plotted");
            $.ajax({
                url: '/swoosh/plot/',
                dataType: 'json',
                success: function(json_data){
                    var data = [{
                        values: Object.values(json_data['json_data']),
                        labels: Object.keys(json_data['json_data']),
                        type: 'pie'
                    }];

                    var layout = {
                        height: 400,
                        width: 500
                    };

                    Plotly.newPlot('imagediv', data, layout);
                }
            });
        }
    });
});
