// solution to Mouse Maze lab

var loser = null;  // whether the user has hit a wall

window.onload = function() {
	document.getElementById("start").onclick = startClick;
	document.getElementById("end").onmouseover = overEnd;
	var boundaries = document.querySelectorAll("div#maze div.boundary");
	for (var i = 0; i < boundaries.length; i++) {
		boundaries[i].onmouseover = overBoundary;
	}
	document.body.onmousemove = overBody;   // haxor exercise
};

// test for mouse being over document.body so that the player
// can't cheat by going outside the maze (haxor exercise)
function overBody(event) {
	if (loser === false && event.target == document.body) {
		overBoundary(event);
	}
}

// called when mouse moves on top of one of the walls;
// signals the end of the game with a loss
function overBoundary(event) {
	if (loser === false) {
		loser = true;
		document.getElementById("status").innerHTML = "You lose!";
		var boundaries = document.querySelectorAll("div#maze div.boundary");
		for (var i = 0; i < boundaries.length; i++) {
			boundaries[i].classList.add("youlose");
		}
		event.stopPropagation();   // so the event won't reach document.body (haxor exercise)
		return false;
	}
}

// called when mouse is clicked on Start (S) div;
// sets the maze back to its initial playable state
function startClick() {
	loser = false;
	document.getElementById("status").innerHTML = "Find the end!";
	var boundaries = document.querySelectorAll("div#maze div.boundary");
	for (var i = 0; i < boundaries.length; i++) {
		boundaries[i].classList.remove("youlose");
	}
}

// called when mouse is on top of the End (E) div.
// signals the end of the game with a win
function overEnd() {
	if (loser === false) {
		document.getElementById("status").innerHTML = "You win! :]";
	}
}
