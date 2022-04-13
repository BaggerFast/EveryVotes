var preload = $("#main_preload"), 
    w = $(window).width() / 2 - 30, 
    h = $(window).height() / 2 - 30;
preload.html('<img src="../img/preloader.gif" alt="load content."/>');
preload.css({"top": h + 'px', "left": w + 'px'});
$(window).load(function () {
    setTimeout(function () {
        preload.animate({opacity: "0"}, 50, function () {
            preload.html("")
        });
        $("#wrapper").animate({opacity: "1"}, 50)
    }, 250)
});