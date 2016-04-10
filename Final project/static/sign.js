function signup() {
     var a = $("#name");
     var b = $("#password");
     if ( !a.val() || !b.val() ) {
        alert("用户名和密码不能为空");
        return false;
     } else {
        var a = $.ajax({
            type: "POST",
            url: "/signup",
            data: { "name": $("#name").val(), "password": $("#password").val()}
        });
    
        a.done(function(data) {
            alert(data);
            if ( data == 'Signup Succeed' ) {
                window.location.href = '/';
                return true;
            }
        });
        return false; 
    }
}

$(document).ready(function() {
    $("#submit").click(signup);
});