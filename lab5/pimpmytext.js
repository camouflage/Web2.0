// 13331231 sunsheng lab5 pimpmytext.js
function $(id) {
	return document.getElementById(id);
}

window.onload = function() {
	alert("Hello World!");
	$("bigger").onclick = delay;
	$("bling").onclick = checkbox;
	$("snoopify").onclick = becomeSno;
	$("mal").onclick = mal;
	$("ia").onclick = ia;
};

// Bigger Pimpin: setInterval, increase font size for every 500ms
var timer = null;
function delay() {
	if ( timer == null ) {
		timer = setInterval(becomeBigger, 500);
	} else {
		clearInterval(timer);
		timer = null;
	}
}

// increase font size by 2pt
function becomeBigger() {
	// in px
	var fontsize = window.getComputedStyle(text, null).getPropertyValue('font-size');
	// 2pt = 3px
	var fontsizepx = parseInt(fontsize)
	fontsizepx += 3;
	$("text").style.fontSize = fontsizepx.toString() + "px";
}

// bling
function checkbox() {
	if ( $("bling").checked ) {
		$("text").className = "blingtext";
		//document.body.style.background = "url('hundred-dollar-bill.jpg')";
		document.body.className = "bodybg";
	} else {
		$("text").className = "original";
		//document.body.style.background = "";
		document.body.className = "";
	}
}

// snoopify
function becomeSno() {
	var str = $("text").value;
	str = str.toUpperCase();
	arr = str.split(".");
	str = arr.join("-izzle.");
	$("text").value = str;
}

// Malkovitch
function mal() {
	var str = $("text").value;
	str = str.replace(/[a-zA-Z]{5,}/g, "Malkovitch");
	$("text").value = str;
}

// Igpay Atinlay
function ia() {
	var str = $("text").value;
	// vowel
	var arr = str.match(/[^a-zA-Z]+[aeiouAEIOU][a-zA-Z]*|^[aeiouAEIOU][a-zA-Z]*/g);
	for ( var i = 0; arr != null && i < arr.length; i++ ) {
		str = str.replace(arr[i], arr[i] + "-ay");
	}
	// consonant
	var arr = str.match(/[^a-zA-Z]+[^aeiouAEIOU][a-zA-Z]*|^[^aeiouAEIOU][a-zA-Z]*/g);
	for ( var i = 0; arr != null && i < arr.length; i++ ) {
		var pos = arr[i].search(/[a-zA-Z]/);
		str = str.replace(arr[i], arr[i].substring(0, pos) +
						  arr[i].substring(pos + 1) + arr[i].charAt(pos) + "-ay");
	}
	$("text").value = str;
}