$(document).ready(function() {
    $("#moodselect").change(changemood);
});
function changemood() {
	var img = $("#img");
    var mood = $("#moodselect option:selected").text();
    if ( mood == "Good" ) {
        img.attr("src", "../static/images/moodgood.gif");
    }
    else if ( mood == "General" ) {
        img.attr("src", "../static/images/general.gif");
    }
    else if ( mood == "Bad") {
        img.attr("src", "../static/images/moodbad.gif");
    }
}