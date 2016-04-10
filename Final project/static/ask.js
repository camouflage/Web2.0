function titleifempty() {
     var a = $("#myTitle");
     var b = $("#content");
     if ( !a.val() || !b.val()) {
        alert("标题和内容不能为空");
        return false;
     } else {
         return true;
     }
    }
    $(document).ready(function() {
    $("#publishNP").click(titleifempty);
});