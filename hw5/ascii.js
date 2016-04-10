// 13331231 sunsheng hw5 ascii.js
// 额外功能: turbo加速, 控制器生效, 非侵入式JavaScript
function $(id) {
    return document.getElementById(id);
}

window.onload = function() {
    // variables
    var count;
    var frame;
    var st;
    var oritext;
    var sp;
    // functions
    $("slct").onchange = changeAnima;
    $("start").onclick = start;
    $("stop").onclick = stop;
    $("s").onclick = small;
    $("m").onclick = middle;
    $("l").onclick = large;
    //$("turbo").onclick = turbo;
    // inhibit stop
    $("stop").disabled = true;
};

function changeAnima() {
    var anima = $("slct").value;
    $("displayarea").value = ANIMATIONS[anima];
}

function start() {
    // original content
    oritext = $("displayarea").value;
    // split animation
    var anima = $("slct").value;
    frame = ANIMATIONS[anima].split("=====\n");

    // start animation
    count = 0;
    st = 1;
    animation();
    // inhibit start & select and restore stop
    $("start").disabled = true;
    $("slct").disabled = true;
    $("stop").disabled = false;
}

function animation() {
    if ( st == 1 ) {
        turbo();
        $("displayarea").value = frame[count];
        count++;
        if ( count >= frame.length ) {
            count = 0;
        }
        setTimeout(animation, sp);
    }
}
// stop the animation
function stop() {
    st = 0;
    $("displayarea").value = oritext;
    // inhibit stop and restore start & select
    $("stop").disabled = true;
    $("start").disabled = false;
    $("slct").disabled = false;
}
// font size
function small() {
    $("displayarea").style.fontSize = "7pt";
}

function middle() {
    $("displayarea").style.fontSize = "12pt";
}

function large() {
    $("displayarea").style.fontSize = "24pt";
}
// Extra feature: Turbo speed
function turbo() {
    if ( $("turbo").checked ) {
        sp = 50;
    } else {
        sp = 200;
    }
}

// my custom animation
ANIMATIONS["Custom"] = 
    "  o  \n" + 
    " /#\\ \n" + 
    " _|_ \n" + 
    "=====\n" + 
    "      o  \n" + 
    "     /#\\ \n" + 
    "      | \\\n" + 
    "     _|_\n" + 
    "=====\n" + 
    "          o  \n" + 
    "         /#\\ \n" + 
    "          | \\\n" + 
    "          |  \\\n" + 
    "         _|_\n" + 
    "=====\n" + 
    "              o  \n" + 
    "             /#\\ \n" + 
    "              | \\\n" + 
    "              |  \\\n" + 
    "              |   \\\n" + 
    "             _|_\n";