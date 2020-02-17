$('DIV#toggle_header').on('click', function() {
    if ($('header').hasClass('green')) {
        $('header').removeClass();
        $('header').addClass('red');
    } else {
        $('header').removeClass();
        $('header').addClass('green');

    }
});