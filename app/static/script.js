// var path = document.getElementById('path');
// console.log(path);
$(document).ready(function(){
    var pathobj = $("#path").text();
    // var pathobj = "['301', '302']";
    pathobj = pathobj.replace(/'/g, '"');
    pathobj = JSON.parse(pathobj);
    console.log(pathobj);

    // var temp = pathobj[0] + 'to' + pathobj[1];
    //
    // console.log("#" + temp);
    // var thisId = ("#" + temp);
    //
    // if ($(thisId)) {
    //     $(thisId).addClass('hidden');
    // }

    // console.log($("#pathline").children()[10].id);
    var linelen = $("#pathline").children().length;
    for (var j = 0; j < pathobj.length; j++) {
        for (var i = 0; i < linelen; i++) {
            if ($("#pathline").children()[i].id.search(pathobj[j]) != -1 && $("#pathline").children()[i].id.search(pathobj[j-1]) != -1) {
                console.log('yes');
                console.log($("#pathline").children()[i]);
                console.log($("#pathline").children()[i].id);
                $('#' + $("#pathline").children()[i].id).addClass('hidden');
            }
        }
    }


});

