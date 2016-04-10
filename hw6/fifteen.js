// 13331231 sunsheng hw6 fifteen.js
// 额外功能: 结束游戏提示且h1增加背景(必须先shuffle)
function $(id) {
    return document.getElementById(id);
}

function $$(selector) {
    return document.querySelectorAll(selector);
}

window.onload = function() {
    var vacantid;
    var start;
    init();
    // handle highlighting styles
    var puz = $$("div#puzzlearea div");
    for ( var i = 0; i < puz.length; i++ ) {
        puz[i].onmouseover = function(event) {
            if ( can(parseInt(event.target.id)) ) {
                event.target.classList.add("movablepiece");
                event.target.style.borderColor = "red";
            }
        }
        puz[i].onmouseout = function(event) {
            if ( can(parseInt(event.target.id)) ) {
                event.target.classList.remove("movablepiece");
                event.target.style.borderColor = "black";
            }
        }
        puz[i].onclick = move;
    }
    $("shufflebutton").onclick = shuffle;
    /*
    var pic = document.getElementsByTagName("button");
    pic[1].onclick = function() {
        picarr = "url(background.jpg)";
    }
    pic[2].onclick = function() {
        picarr = "url(background1.jpg)";
    }
    pic[3].onclick = function() {
        picarr = "url(background2.jpg)";
    }
    pic[4].onclick = function() {
        picarr = "url(background3.jpg)";
    }
    */
};

// initialize the game
function init() {
    // create a div for the vacant part
    var puz = $$("div#puzzlearea div");
    var div15 = document.createElement("div");
    $("puzzlearea").appendChild(div15);
    // set background position to show the pic correctly
    puz = $$("div#puzzlearea div");
    for ( var i = 0; i < puz.length; i++ ) {
        puz[i].classList.add("puzzlepiece");
        puz[i].style.left = i * 100 % 400 + "px";
        puz[i].style.top = Math.floor(i / 4) * 100 + "px";
        puz[i].style.backgroundPosition = i * (-100) % 400 + "px "+ Math.floor(i / 4) * (-100) + "px";
        puz[i].id = i;   
    }
    puz[15].style.background = "none";
    puz[15].style.borderColor = "white";
    vacantid = 15;

    start = 0;
    //createpic();
    //picarr = "url(background.jpg)";
}

// move
function move() {
    var puz = $$("div#puzzlearea div");
    var id = parseInt(event.target.id);
    // exchange the style and innerHTML between two divs
    if ( can(id) ) {
        puz[vacantid].style.background = puz[id].style.background;
        puz[vacantid].style.backgroundImage = "url(background.jpg)";
        puz[vacantid].style.borderColor = "black";
        puz[vacantid].innerHTML = puz[id].innerHTML;
        puz[id].style.background = "none";
        puz[id].style.borderColor = "white";
        puz[id].innerHTML = "";
        vacantid = id;
        if ( finish() ) {
            alert("You win! To begin just click shuffle.");
            start = 0;
            document.getElementsByTagName("h1")[0].style.background = "url(win.jpg)";
        }
    }
}

// decide whether can move or not
function can(id) {
    if ( id == vacantid ) {
        return false;
    }
    // disable
    var up = -4, down = 4, left = -1, right = 1;
    if ( id % 4 == 0 ) {
        left = 0;
    }
    if ( id % 4 == 3 ) {
        right = 0;
    }
    if ( Math.floor(id / 4) == 0 ) {
        up = 0;
    }
    if ( Math.floor(id / 4) == 3 ) {
        down = 0;
    }
    // final judge
    if ( vacantid == id + up || vacantid == id + down ||
         vacantid == id + left || vacantid == id + right ) {
        return true;
    } else {
        return false;
    }
}

// shuffle
function shuffle() {
    // imitate mouse click
    for ( var i = 0; i < 2000; i++ ) {
        var id = Math.floor(Math.random() * 16);
        $(id).click();
    }
    start = 1;
    document.getElementsByTagName("h1")[0].style.background = "";
}

// extra feature: handle finish
function finish() {
    if ( start == 1 ) {
        var puz = $$("div#puzzlearea div");
        for ( var i = 0; i < puz.length; i++ ) {
            if ( i == vacantid ) {
                continue;
            }
            if ( parseInt(puz[i].innerHTML) - 1 != i ) {
                return false;
            }
        }
        return true;
    } else {
        return false;
    }
}
/*
// extra feature: different pic
function createpic() {
    var control = $("controls");
    var picdiv = document.createElement("div");
    control.appendChild(picdiv);
    var but = new Array();
    for ( var i = 0; i < 4; i++ ) {
        but[i] = document.createElement("button");
        but[i].innerHTML = "pic" + i;
        but[i].id = i;
        picdiv.appendChild(but[i]);
    }
}
*/