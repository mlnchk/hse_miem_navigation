$(document).ready(function(){

    var start = $('#start-data').text(), finish = $('#finish-data').text();

    console.log(Math.floor(start / 100));
    console.log(Math.floor(finish / 100));

    var startFloor = Math.floor(start / 100);
    var finishFloor = Math.floor(finish / 100);

    console.log($('#' + start).parent()[0]);
    console.log($('#' + finish).parent()[0]);

    var lol = $('#path')[0].innerText;
    lol = lol.slice(1, lol.length - 1).replace(/\s+/g,'');
    lol = lol.split(',');
    console.log(lol);

    if ($('#' + start).parent()[0] == $('#' + finish).parent()[0]) {
        $('#' + start).parent().removeClass('st0');
        $('svg').children().children().css('opacity', '0.2');
        $('#main').children().css('opacity', '1');
        $('#' + start).css('opacity', '1');
        $('#' + finish).css('opacity', '1');
    } else {
        $('#next-step').removeClass('hidden');
        $('#' + start).parent().removeClass('st0');
        $('svg').children().children().css('opacity', '0.2');
        $('#main').children().css('opacity', '1');
        $('#' + start).css('opacity', '1');

        for (var i = 0; i < lol.length; i++) {
            console.log(lol[i]);
            if (lol[i] == "'LE'") {
                console.log('yes');
                $('#LE').css('opacity', '1');
            }
        }

        $('#next-step').click(function () {
            $('#' + start).parent().addClass('st0');
            $('#' + finish).parent().removeClass('st0');
            $('#' + finish).css('opacity', '1');
        })
    }

});

