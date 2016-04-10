function $(id) {
    return document.getElementById(id);
}

function $$(selector) {
    return document.querySelectorAll(selector);
}

var success = -1;

window.onload = function() {
    var allbound = $$("div#maze div.boundary");
    for ( var i = 0; i < allbound.length; i++ ) {
        allbound[i].onmouseover = turnRed;
    }
    $("end").onmouseover = judgesuc;
    $("start").onclick = start;
};

function turnRed() {
    if ( success == 1 ) {
        var allbound = $$("div#maze div.boundary");
        for ( var i = 0; i < allbound.length; i++ ) {
            allbound[i].classList.add("youlose");
        }
        success = 0;
        $("status").innerHTML = "You lose!";
    }
}

function judgesuc() {
    if ( success == 1 ) {
        $("status").innerHTML = "You win!";
        success = -1;
    }
}

function start() {
    $("status").innerHTML = "Move your mouse over the \"S\" to begin.";
    var allbound = $$("div#maze div.boundary");
    for ( var i = 0; i < allbound.length; i++ ) {
        allbound[i].classList.remove("youlose");
    }
    success = 1;
    cheat();
}

function cheat() {
    var maze = $("maze");
    maze.onmouseover = function(event) {
        event.stopPropagation();
    };
    var body = document.getElementsByTagName("body")[0]
    body.onmouseover = turnRed;
}
