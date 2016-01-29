$(function(){

    $(".button-collapse").sideNav();
    var link = window.location.pathname;
    link = link.substr(0, link.length -1);

    $('.side-nav li a[href="' + link + '"]').addClass('active');

});