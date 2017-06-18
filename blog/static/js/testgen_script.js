$(document).ready(function(){

    // default values for all the controls
    $("#no_of_tests").val(1)
    $("#no_of_tests").attr("disabled", true)
    $("#array_range_from").val(0)
    $("#array_range_to").val(1e9)
    $("#integer_range_from").val(0)
    $("#integer_range_to").val(1e9)
    $("#array_no_of_items").val(10)
    $("#string_no_of_items").val(10)
    $("#string_lower").prop("checked", true)


    // basic customizations

    // some exclusions
    $("#test_no_checkbox").on('change', function(){
        if($(this).prop("checked")){
            $("#no_of_tests").attr("disabled", false)
        }else{
            $("#no_of_tests").attr("disabled", true)
        }
    })
    $("#string_binary").on("change", function(){
        if($(this).prop("checked")){
            $(".string_controls").attr("disabled", true)
            $(this).attr("disabled", false)
        }else{
            $(".string_controls").attr("disabled", false)
        }
    })
    $("#string_custom").on("change", function(){
        if($(this).prop("checked")){
            $(".string_controls").attr("disabled", true)
            $(this).attr("disabled", false)
            $("#custom_symbols").attr("disabled", false)
        }else{
            $(".string_controls").attr("disabled", false)
            $("#custom_symbols").attr("disabled", true)
        }
    })


    var generate = function(){
        console.log("Sending request")
        var include_tests = $("#test_no_checkbox").prop("checked")
        var no_of_tests = 1
        if(include_tests){
            no_of_tests = $("#no_of_tests").val()
        }
        console.log("no of tests " + no_of_tests)
        var case_type = $("#case_type").val()
        var context = {}
        var vertical = false
        if($("#array_vertical").prop("checked"))
            vertical = true
        if(case_type == "array"){
            $(".case_types").show()
            $(".case_types:not(.array_type)").hide()
            context = {
                "no_of_items": $("#array_no_of_items").val(),
                "from": $("#array_range_from").val(),
                "to": $("#array_range_to").val(),
                "vertical": vertical
            }
        }else if(case_type == "integer"){
            $(".case_types").show()
            $(".case_types:not(.integer_type)").hide()
            context = {
                "from": $("#integer_range_from").val(),
                "to": $("#integer_range_to").val()
            }
        }else if(case_type == "string"){
            $(".case_types").show()
            $(".case_types:not(.string_type)").hide()
            context = {
                "no_of_items": $("#string_no_of_items").val(),
                "lower": $("#string_lower").prop("checked"),
                "upper": $("#string_upper").prop("checked"),
                "digits": $("#string_digits").prop("checked"),
                "symbols": $("#string_symbols").prop("checked"),
                "binary": $("#string_binary").prop("checked"),
                "custom": $("#string_custom").prop("checked"),
                "custom_text": $("#custom_symbols").val()
            }
        }
        $.ajax({
            url: "/testgen/generate/",
            type: "POST",
            data: {
                "include_tests": include_tests,
                "no_of_tests": no_of_tests,
                "case_type": case_type,
                "context": context,
                "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function(response){
                $("#test-data").html(response["content"]);
            }
        })
    }
    // generate on document load
    generate()
    $("select").on("change", function(){
        generate()
    })
    $("input").on("change", function(){
        generate()
    })
    $("input").on("keyup", function(){
        generate()
    })
    $("#submit-btn").on("click", function(){
        generate()
    })

    $(document).bind("keydown", null, function(e){
        if(e.altKey && e.keyCode == 67){
            $("#copy-button").click()
            $("#copy-alert").show(0).delay(1000).fadeOut(1000)
        }
    })
})