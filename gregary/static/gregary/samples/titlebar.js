function drawLoginButton() {
    // Create login-button
    var login_button = document.createElement('button');
    login_button.className = 'custom-button';
    login_button.id = 'login-button';
    
    //TODO: move button when active
    
    // Put in text
    var login_button_text = document.createTextNode('LOGIN');
    login_button.appendChild(login_button_text);
    
    // Put the button into the webpage
    document.getElementById('uinfo-outer-container').appendChild(login_button);
}

//document.onload += drawLoginButton();
/*
document.onload += function() {
    if (isLoggedIn) {
        drawUserInfo();
    } else{
        drawLoginButton();
    }
}
*/
document.onload += console.log("Loaded");