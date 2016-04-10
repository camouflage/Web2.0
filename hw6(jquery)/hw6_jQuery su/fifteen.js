// 实现功能一，完成游戏提示
// To Players:
// you can change shuffletime to complete the game easily.
var shuffletime = 2000;
var empty = 15;
var position = ["0px 0px", "-100px 0px", "-200px 0px", "-300px 0px",
				"0px -100px", "-100px -100px", "-200px -100px", "-300px -100px",
				"0px -200px", "-100px -200px", "-200px -200px", "-300px -200px",
				"0px -300px", "-100px -300px", "-200px -300px", "-300px -300px"];
var winid;

function build() {
	$("#puzzlearea").children().each(function(i, element) {
		var pic = $(element);
		pic.attr("class", "puzzlepiece");
		pic.css("top", Math.floor(i / 4) * 100);
		pic.css("left", i % 4 * 100);
		pic.css("backgroundPosition", position[i]);
	});
}
function move() {
	var pos = parseInt(this.style.top) / 100 * 4 + parseInt(this.style.left) / 100;
	if (around(pos)) {
		var pic = $(this);
		pic.css("top", Math.floor(empty / 4) * 100);
		pic.css("left", empty % 4 * 100);
		empty = pos;
	}
}
function hover() {
	var pos = parseInt(this.style.top) / 100 * 4 + parseInt(this.style.left) / 100;
	if (around(pos)) {
		this.setAttribute("class", "puzzlepiece movablepiece");
	}
}
function out() {
	this.setAttribute("class", "puzzlepiece");
}
function around(posi) {
	var row = Math.floor(posi / 4);
	var column = posi - row * 4;
	var erow = Math.floor(empty / 4);
	var ecolumn = empty - erow * 4;
	if (column == ecolumn && Math.abs(row - erow) == 1) {
		return true;
	}
	if (row == erow && Math.abs(column - ecolumn) == 1) {
		return true;
	}
	return false;
}
function shuffle() {
	var pieces = $("#puzzlearea").children();
	for (var i = 0; i < shuffletime; i++) {
		var rand = Math.floor(Math.random() * 15);
		$(pieces[rand]).trigger("click");
	};
	winid = setInterval(win, 200);
}
function win() {
		var all = false;
		var piece = $(".puzzlepiece");
		for (var i = piece.length - 1; i >= 0; i--) {
			var top = parseInt(piece[i].style.top) / 100;
			var left = parseInt(piece[i].style.left) / 100;
			if (top * 4 + left !== i) {
				all = true;
				break;
			}
		};
		if (!all) {
			alert("Congratulation! My friend!\nThank you for enjoying this boring game");
			clearInterval(winid);
			$("body")[0].style.backgroundImage = "url(background.jpg)";
		}
}

$(function() {
	build();
	// add event listener to every puzzle pieces
	$("#puzzlearea").children().each(function(i, element) {
		var pic = $(element);
		pic.bind("click", move);
		pic.bind("mouseover", hover);
		pic.bind("mouseout", out);
	});
	// add listener to shuffle button
	$("#shufflebutton").click(shuffle);
});
