
var already_answered = false;
var storage = sessionStorage.getItem(id);
if (storage !== null && id !== null && id !== "") {
    storage = JSON.parse(storage);
    already_answered = storage.answered;
    if (already_answered) {
        var clicked = $(`#${storage.clicked}`);
        var correct = $(`#${correct_answer}`);
        if (already_answered) {
            if (storage.clicked !== correct_answer) {
                clicked.addClass("bg-danger");
                clicked.addClass("text-white");
            }
            correct.addClass("bg-success");
            correct.addClass("text-white");
        }
    }
}

$(".answer").click(function() {
    if (already_answered) return;
    already_answered = true;
    var correct = $(this).attr("id") === correct_answer;
    if (correct) {
        $(this).addClass("btn-success");
        setTimeout(function () {
            $('#next-exercise')[0].click();
        }, 100);
    } else {
        $(this).addClass("btn-danger");
        $(`#${correct_answer}`).removeClass("bg-light");
        $(`#${correct_answer}`).addClass("btn-success");
    }

    var data = {
        answered: true,
        correct: correct,
        clicked: $(this).attr("id")
    };

    if (sessionStorage.getItem("points") === null) {
        sessionStorage.setItem("points", 0);
    }

    const currentPoints = parseInt(sessionStorage.getItem("points"));
    if (correct && sessionStorage.getItem(id) === null) {
        sessionStorage.setItem("points", currentPoints + points);
    }

    UpdatePoints();

    sessionStorage.setItem(id, JSON.stringify(data));
});