function drawTitleBar(x) {
    ////// Creates the titlebar inside the canvas
    // Cache storing the canvas
    'use strict';
    var titlebar = document.getElementById('titlebar_canvas');
    var ctx = titlebar.getContext('2d');
    
    // Sizing the drawing area
    titlebar.style.width = (window.innerWidth >= 1000) ? window.innerWidth : 1000;
    titlebar.width = titlebar.scrollWidth;
    titlebar.height = titlebar.scrollHeight;
    
    // Clear the canvas
    ctx.clearRect(0, 0, titlebar.width, titlebar.height);
    
    // Drawing the shape
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, titlebar.height - 5);
    ctx.lineTo(250, titlebar.height - 5);
    ctx.lineTo(300, titlebar.height - 5 - x);
    ctx.lineTo(titlebar.width, titlebar.height - 5 - x);
    ctx.lineTo(titlebar.width, 0);
    
    // Styling before fill
    ctx.shadowBlur = 5;
    ctx.shadowColor = "#111111";
    ctx.shadowOffsetY = 1;
    ctx.shadowOffsetX = 1;
    
    ctx.shadowBlur = 0;
    ctx.fillStyle = "#222222";
    ctx.fill();
}

function animateTitleBar(x, y) {
    // Draws title bar with animation
    'use strict';
    function rep() {
        drawTitleBar(x);
        x += 1;
    }
    
    do {
        var timer = setTimeout(rep(), 2000);
    } while (x < y);
}

// Draw the titlebar on load
document.body.onload = animateTitleBar(0, 25);

// Redraw the titlebar on window resize
$(window).resize(function () {
    'use strict';
    drawTitleBar(25);
});