$(document).ready(function(){
    
    $("#plot").on("click", function(){
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
