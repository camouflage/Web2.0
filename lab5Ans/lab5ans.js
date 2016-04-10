"use strict";

var timer;

// Start up javascript code once the page has finished loading
window.onload = function() {
    document.getElementById("pimp").onclick = pimpin;
    document.getElementById("bling").onchange = blingin;
    document.getElementById("snoop").onclick = snoopin;
    document.getElementById("pig").onclick = igpay;
    document.getElementById("malkovitch").onclick = malkovitch;
};

// Pimp out the text by constantly increasing
// the font size every half a second
function pimpin() {
    timer = setInterval(increaseFont, 500);
}

// Increase the font size of the text section by 2pts
function increaseFont() {
    var text = document.getElementById("text");
    if (!text.style.fontSize) {
        text.style.fontSize = "12pt";
    } else {
        text.style.fontSize = parseInt(text.style.fontSize) + 2 + "pt";
    }
}

// Replace words that are 5 characters in length or longer
// to be replaced with Malkovich 
function malkovitch() {
    var text = document.getElementById("text");
    // Split on non word character, but keep the delimiter in 
    // the resulting array for later joining
    var array = text.value.split(/(\W)/);
    for (var i = 0; i < array.length; i++) {
        if (array[i].length >= 5) {
            array[i] = "Malkovich";
        }
    }
    text.value = array.join("");
}

// Convert text to pig latin
function igpay() {
    var text = document.getElementById("text");
    var vowels = "aeiou";
    // Split on non word character, but keep delimiter in
    // resulting array for later joining
    var array = text.value.split(/(\W)/);
    for (var i = 0; i < array.length; i++) {
        // Only pig latin-ize actual words
        if (array[i].match(/[^\W]/)) {
            // Locate vowel
            var vowelIndex = 0;
            // Solution using index of:  && "aeiouAEIOU".indexOf(array[i][vowelIndex]) < 0
            while (vowelIndex < array[i].length && !array[i][vowelIndex].match(/[aeiou]/i)) {
                vowelIndex++;
            }
            // Shift characters before vowel
            array[i] = array[i].substring(vowelIndex) + array[i].substring(0, vowelIndex);

            // Attach -aaaayyy
            array[i] += "ay";
        }
    }
    text.value = array.join("");
}

// Bling out text by changing color between bold and green when selected, black when not
// Change text to strikethrough and underline when selected
// Also changes page background to be $$ when selected
function blingin() {
    var body = document.getElementsByTagName("body")[0];
    body.style.backgroundImage = 
            "url('https://webster.cs.washington.edu/images/pimpmytext/hundred-dollar-bill.jpg')";
    var text = document.getElementById("text");
    if (document.getElementById("bling").checked) {
        text.style.fontWeight = "bold";
        text.style.color = "green";
        text.style.textDecoration = "underline line-through";
    } else {
        text.style.fontWeight = "nomal";
        text.style.color = "black";
        text.style.textDecoration = "none";
    }
}

// Snoopify the text by adding -izzle to the end of sentences.
function snoopin() {
    var text = document.getElementById("text");
    var array = text.value.split(".");
    text.value = array.join("-izzle.");
}