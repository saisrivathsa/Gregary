//						JS for the LoginNPU
//
//// Name declarations:
// LoginNPU : Id of main LoginNPU div
//
var LoginNPU = document.getElementById("LoginNPU");

function showLoginApplet() {
	$("#LoginNPU").fadeIn(96);
}

$(document).keyup(function(e){
	if(e.keyCode == 27) {
		if($("#LoginNPU").is(":visible")){
			$("#LoginNPU").fadeOut(96);
		}
	}
});
