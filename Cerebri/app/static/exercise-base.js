
function array_remove(array, index) {
    var newArray = [];
    for (var i = 0; i < array.length; i++) {
        if (i === index) continue;
        newArray.push(array[i]);
    }
    return newArray;
}


function compare(a, b) {
    if (typeof a === 'undefined' && typeof b === 'undefined') return true;
    if (typeof a === 'undefined' || typeof b === 'undefined') return false;
    if (a === null && b === null) return true;
    if (a === null || b === null) return false;
    if (a === b) return true;
    if (a.includes('inf') && !b.includes('inf')) return false;
    if (b.includes('inf') && !a.includes('inf')) return false;
    try {
        a = a.replace('%', 'percent');
        b = b.replace('%', 'percent');

        var parser = math.parser();
        parser.evaluate('percent = 0.01');

        a = parser.evaluate(a);
        b = parser.evaluate(b);

        if (a === b) return true;
        if (math.compare(a, b) === 0) return true;
    } catch (e) {
        return false;
    }
    return false;
}

if (sessionStorage.getItem('points') === null) {
    sessionStorage.setItem('points', 0);
}


$(document).ready(function () { });
MathJax.Hub.Queue(function () {
    $('#exercise').css('visibility', 'initial');
});

function UpdatePoints() {
    let points = parseInt(sessionStorage.getItem('points'));
    if (isNaN(points)) {
        sessionStorage.setItem('points', 0);
        points = 0;
    }

    $('#points').text(points);
}

UpdatePoints();

$('#end-course').click(function (event) {
    event.preventDefault();
    if (confirm("Przechodząc dalej kończysz kurs. Kontynuować?")) {
        var points = parseInt(sessionStorage.getItem('points'));
        var percent = Math.floor(points * 100 / total_points);
        alert(`Gratulacje! Twój wynik to ${points} punktów z ${total_points} możliwych: ${percent}%.`);
        window.location = "/";
    }
});