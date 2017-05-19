$(document).ready(function() {

    var start = $('#start-data').text(), finish = $('#finish-data').text();


    if (start != 'undefined' && finish != 'undefined') {
        $('#stage-1').addClass('st0');
        $('#stage-1a').addClass('st0');
    }

    var lol = $('#path')[0].innerText;
    lol = lol.slice(1, lol.length - 1).replace(/\s+/g, '');
    lol = lol.split(',');
    console.log(lol);

    var startFloor = $('#' + start).parent(), finishFloor = $('#' + finish).parent();

    if (startFloor[0] == finishFloor[0]) {
        $('svg').children().children().css('opacity', '0.2');
        $('#main').children().css('opacity', '1');
        startFloor.removeClass('st0');
        $('#' + start).css('opacity', '1');
        $('#' + finish).css('opacity', '1');
    } else {
        $('#next-step').removeClass('hidden');
        $('svg').children().children().css('opacity', '0.2');
        $('#main').children().css('opacity', '1');
        $('#' + start).css('opacity', '1');
        startFloor.removeClass('st0');

        var temp = 0;

        // лифты лестницы
        if (startFloor[0].id.length < finishFloor[0].id.length
        	|| startFloor[0].id.length == finishFloor[0].id.length) {
            for (var i = 0; i < lol.length; i++) {
                if (lol[i] == "'LE'" || lol[i] == "'LW'" || lol[i] == "'LN'" || lol[i] == "'LS'" || lol[i] == "'Lu'" || lol[i] == "'LWa'") {
                    var node = lol[i];
                    $('#' + node.replace("'", "").replace("'", "")).css('opacity', '1');
                    // temp += 1;
                    break

                }
            }
        } else if (startFloor[0].id.length > finishFloor[0].id.length) {
            $('#LWa').css('opacity', '1');
        }


        $('#next-step').click(function () {
            if (startFloor[0].id.length == finishFloor[0].id.length) {
                startFloor.addClass('st0');
                finishFloor.removeClass('st0');
                $('#' + finish).css('opacity', '1');
                $('#next-step').addClass('hidden');
            } else if (startFloor[0].id.length > finishFloor[0].id.length) {
                for (var i = 0; i < lol.length; i++) {
                    if (lol[i] == "'LE'" || lol[i] == "'LW'" || lol[i] == "'LN'" || lol[i] == "'LS'" || lol[i] == "'Lu'") {
                        $('#' + lol[i].replace("'", "").replace("'", "")).css('opacity', '1');
                        break
                    }
                }

                startFloor.addClass('st0');
                $('#stage-1').removeClass('st0');
                $('#center').css('opacity', '1');
                $('#stage-1a').removeClass('st0');
                $('#LWa').css('opacity', '1');

                $('#next-step').click(function () {
                    $('#LWa').css('opacity', '0');
                    // $('#' + lol[i].replace("'", "").replace("'", "")).css('opacity', '0');
                    $('#stage-1').addClass('st0');
                    $('#stage-1a').addClass('st0');
                    finishFloor.removeClass('st0');
                    $('#' + finish).css('opacity', '1');
                    $('#next-step').addClass('hidden');
                });
            } else if (startFloor[0].id.length < finishFloor[0].id.length) {

                startFloor.addClass('st0');
                $('#stage-1a').removeClass('st0');
                $('#center').css('opacity', '1');
                $('#stage-1').removeClass('st0');
                $('#LWa').css('opacity', '1');

                $('#next-step').click(function () {
                    $('#stage-1').addClass('st0');
                    finishFloor.removeClass('st0');
                    $('#' + finish).css('opacity', '1');
                    $('#next-step').addClass('hidden');
                    $('#' + node.replace("'", "").replace("'", "")).css('opacity', '0');

                });
            }
            // $('#stage-1a').addClass('st0');

        });

    }
});

