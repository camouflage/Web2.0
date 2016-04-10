// 13331231 sunsheng hw6 fifteen.js
// jquery version
$(document).ready(function() {
    var vacantid;
    init();
    // handle highlighting styles
    var puz = $("div#puzzlearea div");
    for ( var i = 0; i < puz.length; i++ ) {
        $(puz[i]).mouseover(function(event) {
            if ( can( parseInt(event.target.id) ) ) {
                $(event.target).addClass("movablepiece");
                $(event.target).css("border-color", "red");
            }
        });
        $(puz[i]).mouseout(function(event) {
            if ( can(parseInt(event.target.id)) ) {
                $(event.target).removeClass("movablepiece");
                $(event.target).css("border-color", "black");
            }
        });
        $(puz[i]).bind("click", function(event) { move(event); });
    }
    $("#shufflebutton").click(shuffle);
});

// initialize the game
function init() {
    // create a div for the vacant part
    $("div#puzzlearea").append("<div></div>");
    // set background position to show the pic correctly
    var puz = $("div#puzzlearea div");
    for ( var i = 0; i < puz.length; i++ ) {
        $(puz[i]).addClass("puzzlepiece");
        $(puz[i]).attr("id", i);
        $(puz[i]).css({
                "left": i * 100 % 400 + "px",
                "top": Math.floor(i / 4) * 100 + "px",
                "background-position": i * (-100) % 400 + "px "+ Math.floor(i / 4) * (-100) + "px",
        });
    }
    $(puz[15]).css({
            "background": "none",
            "border-color": "white"
    });
    vacantid = 15;
}

// move
function move(event) {
    var puz = $("div#puzzlearea div");
    var id = parseInt(event.target.id);
    // exchange the style and innerHTML between two divs
    if ( can(id) ) {
        $(puz[vacantid]).css({
                            "background": $(puz[id]).css("background"),
                            "background-image": "url(background.jpg)",
                            "border-color": "black"
        });
        $(puz[vacantid]).html( $(puz[id]).html() );
        $(puz[id]).css({
                            "background": "none",
                            "border-color": "white"
        });
        $(puz[id]).html( "" );
        vacantid = id;
    }
}

// decide whether can move or not
function can(id) {
    if ( id == vacantid )
        return false;
    var up = -4, down = 4, left = -1, right = 1;
    if ( id % 4 == 0 )
        left = 0;
    if ( id % 4 == 3 )
        right = 0;
    if ( Math.floor(id / 4) == 0 ) 
        up = 0;
    if ( Math.floor(id / 4) == 3 )
        down = 0;
    if ( vacantid == id + up || vacantid == id + down ||
         vacantid == id + left || vacantid == id + right )
        return true;
    else
        return false;
}

// shuffle
function shuffle() {
    var puz = $("div#puzzlearea div");
    for ( var i = 0; i < 1000; i++ ) {
        var id = Math.floor(Math.random() * 16);
        $("#" + id).trigger("click");
    }
}
