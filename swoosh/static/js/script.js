$(document).ready(function(){
	console.log("Only one modal is bound to appear");
	$(".modal-link").click(function(){
		console.log("Script is executing");
		setTimeout(function(){$(".modal").hide();}, 2000);

//		$(this).next(".bs-example-modal-lg").delay(1000).show();
	});
});
