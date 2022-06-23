/*========================
# script distribué dans tous les fichiers
===========================*/

// 1- if no page, show the message

$(document).ready(function(){
    var verify = $("#chk_td").length;
    if (verify == 0){
        $("#no_data").text("No patient found");
        console.log('yo');
    }
});

// 2- time running at realtime

setInterval(function(){
    var date = new Date();
    $("#clock").html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" + (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500)
