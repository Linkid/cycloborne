$(document).ready(function () {

    window.setTimeout(function() {
        $("#success-alert").fadeTo("fast", 500).slideUp(500, function(){
            $("#success-alert").slideUp(500);
        });
    }, 1000);

});
