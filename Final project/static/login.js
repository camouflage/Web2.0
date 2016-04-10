function login() {
     var a = $("#name");
     var b = $("#password");
     if ( !a.val() || !b.val() ) {
        alert("用户名和密码不能为空");
        return false;
     } else {
        var a = $.ajax({
            type: "POST",
            url: "/login",
            data: { "name": $("#name").val(), "password": $("#password").val()}
        });
    
        a.done(function(data) {
            if ( data == '0' ) {
                window.location.href = '/';
                return true;
            }
            alert(data);
        });
        return false; 
    }
}

$(document).ready(function() {
    $("#submit").click(login);
});