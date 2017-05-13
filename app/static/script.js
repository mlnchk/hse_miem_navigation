$(document).ready(function(){

    var start = $('#start-data').text(), finish = $('#finish-data').text();

    console.log(Math.floor(start / 100));
    console.log(Math.floor(finish / 100));

    var startFloor = Math.floor(start / 100);
    var finishFloor = Math.floor(finish / 100);

    if (startFloor != finishFloor) {
        $('#next-step').removeClass('hidden');
    }

    $('#' + start).parent().removeClass('st0');
    $('#' + finish).parent().removeClass('st0');

    $('svg').children().children().css('opacity', '0.2');
    $('#main').children().css('opacity', '1');

    $('#' + start).css('opacity', '1');
    $('#' + finish).css('opacity', '1');

});

