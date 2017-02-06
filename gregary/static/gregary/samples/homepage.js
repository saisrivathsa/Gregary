function activityCardBg(canvasId, image, w = 150, h = 200) {
    // Draws the card shape for a given activity
    var a = 20;

    // Get canvas and its context
    var canvas = document.getElementById(canvasId),
        ctx = canvas.getContext('2d');
    ctx.save();
    
    // Size the canvas and the drawing area
    canvas.style.width = w+2;
    canvas.style.height = h+2;
    canvas.width = canvas.scrollWidth;
    canvas.height = canvas.scrollHeight;


    // Draw the bigger shape
    ctx.beginPath();
    ctx.moveTo(a, 0);
    ctx.lineTo(w, 0);
    ctx.lineTo(w, h-a);
    ctx.lineTo(w-a, h);
    ctx.lineTo(0, h);
    ctx.lineTo(0, a);
    ctx.closePath();

    // Fill this shape
    ctx.shadowColor = 'rgba(0,0,0,0.1)';
    ctx.shadowBlur = 2;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 1;
    ctx.fillStyle = '#fff';
    ctx.fill();

    ctx.shadowBlur = 0;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 0;

    //// Draw icon

    // Draw image
    function load_and_draw(image) {
        if(!image.complete){
            setTimeout( function(){
                load_and_draw(image);
            }, 50);
            return;
        }

        ctx.drawImage(image, 0, 0, w, w);

        // Drawing upper triangle
        ctx.restore();
        ctx.globalCompositeOperation = 'destination-out';
        ctx.beginPath();
        ctx.moveTo(0,0);
        ctx.lineTo(a, 0);
        ctx.lineTo(0, a);
        ctx.fillStyle = 'white';
        ctx.fill();
    }

    var icon = new Image();
    icon.src = image;
    load_and_draw(icon);
    
}

function activityCard(card_name, card_id, icon_image_url, parent_id) {
    // Draws and returns the entire activity card
    
    // Card div
    var card = document.createElement('div');
    card.className += 'card ';    
    document.getElementById(parent_id).appendChild(card);
    
    var cent = document.createElement('center');
    card.appendChild(cent);
    
    // Card content div
    var card_content = document.createElement('div');
    card_content.className += 'card-content';
    cent.appendChild(card_content);
    
    // Link tag
    var link_tag = document.createElement('a');
    link_tag.href = "http://www.google.com";
    card_content.appendChild(link_tag);
    
    // Canvas
    var bg = document.createElement('canvas');
    bg.id = card_id;
    link_tag.appendChild(bg);
    activityCardBg(card_id, icon_image_url, 150, 200);
    
    // Label
    var label = document.createElement('p'),
        label_text = document.createTextNode(card_name.toUpperCase());
    label.className += 'card-name ';
    if (card_name.length > 8) {
        label.className += 'type2 ';
    }
    
    label.appendChild(label_text);
    link_tag.appendChild(label);
    
    return card;
    
}

document.body.onload += activityCard('sports', 'sports', './sports-back.png', 'main-container');
document.body.onload += activityCard('video games', 'vid-games', './sports-back.png', 'main-container');
document.body.onload += activityCard('music', 'music', './sports-back.png', 'main-container');
document.body.onload += activityCard('split-a-meal', 'meal', './sports-back.png', 'main-container');
document.body.onload += activityCard('concert', 'con', './sports-back.png', 'main-container');

document.body.onload += activityCard('movie', 'movie', './sports-back.png', 'main-container');


document.body.onload += (function () {
                   document.getElementById('main-container-bg').style.height = (window.innerHeight+65 < document.getElementById('main-container').style.height) ? document.getElementById('main-container').style.height : window.innerHeight - 65;
                   }());

// On resize events
/*
window.onresize = function () {
    // Resizing main-container-bg (grey colored box)
    document.getElementById('main-container-bg').style.height = (window.innerHeight < 600) ? 600 : window.innerHeight - 65;
};
*/