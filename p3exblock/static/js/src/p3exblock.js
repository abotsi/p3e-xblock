/* Javascript for P3eXBlock. */
function P3eXBlock(runtime, element) {

    // Saving the URL of the handler
    var urlValid1 = runtime.handlerUrl(element, 'validate_phase1');
    var urlValid2 = runtime.handlerUrl(element, 'validate_phase2');
    var urlValid3 = runtime.handlerUrl(element, 'validate_phase3');

    function change_phase(data) {
        console.log("data : ", data)
        // Replacing the html content by the html of the new phase
        $(".p3exblock_block").replaceWith(data['content']);
        $("html, body").animate({ scrollTop: 0 }, "slow");

        // Setting the handler to call on #btn_valid click
        if (data['phase_number'] == 1) {
            $('#btn_valid', element).click(P3eXBlock.validate_phase1);
        } else if (data['phase_number'] == 2) {
            $('#btn_valid', element).click(P3eXBlock.validate_phase2);
        } else if (data['phase_number'] == 3) {
            $('#btn_valid', element).click(P3eXBlock.validate_phase3);
        }
    }

    P3eXBlock.validate_phase1 = function(eventObject) {
        $.ajax({
            type: "POST",
            url: urlValid1,
            data: JSON.stringify([
                // Sending to server a list of JSON object, each contening the answer 
                // gave by the student and grade related to a question
                {'answer': $('#r1').val(), 'question_grade': $('#note_saver1').val()},
                {'answer': $('#r2').val(), 'question_grade': $('#note_saver2').val()},
                {'answer': $('#r3').val(), 'question_grade': $('#note_saver3').val()}
            ]),
            success: change_phase
        });
    }

    P3eXBlock.validate_phase2 = function(eventObject) {
        $.ajax({
            type: "POST",
            url: urlValid2,
            data: JSON.stringify({
                "question": $('#q').val(), 
                "answer": $('#r').val()
            }),
            success: change_phase
        });
    }

    P3eXBlock.validate_phase3 = function(eventObject) {

        $.ajax({
            type: "POST",
            url: urlValid3,
            success: function(){alert("Fini!")}
        });
    }

    $('#btn_valid', element).click(P3eXBlock.validate_phase1);

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
