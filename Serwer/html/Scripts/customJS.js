$("#btn1").click(function () {
    $.ajax({
        url: "GetInfo",
        type: "POST",
        success: function (result) {
            $("#XHResponse").html(result);
        },
        error: function (xhr, status, error) {
            var msg = "Failed with status: " + status + "<br/>"
                + "Error" + error;
            $("#XHResponse").html(msg);
        },
        complete: function (xhr, status) {
            var doneMsg = "Operation complete with status" + status;
            alert(doneMsg);
        }
    });
});