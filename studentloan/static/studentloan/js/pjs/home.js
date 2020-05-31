$(document).ready(function(){
    $("#registerBtn").click(function(){
        $('#intro').hide();
        $('#registerForm').show();        
        
                
    });
    $('.collapseDown').click(function(){
        var href =$(this).attr('href')
         
        $('.collapse').not(href).hide();
        $(this).hide();
        $('.collapseUp').show();
    });
    $('.collapseUp').click(function(){
        $(this).hide();
        $('.collapseDown').show()
    });
    $(window).resize(function(){
        console.log($(window).width());
    });
});