$(function(){

    $(".button-collapse").sideNav();
    var link = window.location.pathname;
    link = link.substr(0, link.length -1);

    $('.side-nav li a[href="' + link + '"]').addClass('active');


    $(window).resize(function(){
        centerBlock();
    });
    // Для запуска функции при загрузке окна:
    $(window).resize();

    //центровка формы логина
    function centerBlock(){
        $('.login-form__wrap').css({
                               position:'absolute',
                               left: ($(window).width() - $('.login-form__wrap').outerWidth())/2,
                               top: ($(window).height() - $('.login-form__wrap').outerHeight())/2
                });
    }
});