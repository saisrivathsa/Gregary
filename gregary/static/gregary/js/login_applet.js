//						JS for the LoginNPU
//
//// Name declarations:
// LoginNPU : Id of main LoginNPU div
// 
var LoginNPU = document.getElementById("LoginNPU");

function showLoginApplet() {
	$("#LoginNPU").fadeIn(96);
}

// Close LoginNPU when the user clicks outside the div
$(document).on('click', function(e){
	if(!LoginNPU.contains(e.target)){
		if($("#LoginNPU").is(":visible")){
			$("#LoginNPU").fadeOut(96);
		}
	}
});

// Close LoginNPU when escape is pressed
$(document).keyup(function(e){
	if(e.keyCode == 27) {
		if($("#LoginNPU").is(":visible")){
			$("#LoginNPU").fadeOut(96);	
		}
	}
});

/*
	
	var mainDiv_Title = document.createElement("H1");
	mainDiv_Title.appendChild(mainDiv_TitleText);


//	mainDiv.innerHTML = "<h1>Enter your login details</h1>";



*/