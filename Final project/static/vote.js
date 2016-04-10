function vote(fid) {
    var aurl = window.location.pathname;
    id = aurl.substr(1);
    id = parseInt(id);
    var a = $.ajax({
        type: "POST",
        url: "/" + id,
    });
    
    a.done( function(data) {
        alert(data);
	});
	return false;

    /*
    var = myurl = "/" + id;
    $.ajax({
        type: "POST",
        url: myurl,
        
        success: function(data) {
            alert(data);
        }
    });
    return false;
    */
}

$(document).ready(function() {
    $(".submit").click( function() {
        vote($(this).attr("id"));
    });
});