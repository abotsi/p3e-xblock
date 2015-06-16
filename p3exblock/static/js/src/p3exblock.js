/* Javascript for P3eXBlock. */
function P3eXBlock(runtime, element) {

    var urlValid1 = runtime.handlerUrl(element, 'validate_phase1');
    var urlValid2 = runtime.handlerUrl(element, 'validate_phase2');
    var urlValid3 = runtime.handlerUrl(element, 'validate_phase3');

    $('#btn_valid1', element).click(function(eventObject) {
        r1 = $('#r1').val();
        r2 = $('#r2').val();
        r3 = $('#r3').val();

        n1 = $('#note_saver1').val();
        n2 = $('#note_saver2').val();
        n3 = $('#note_saver3').val();

        $.ajax({
            type: "POST",
            url: urlValid1,
            data: JSON.stringify(
                {
                    "r1": $('#r1').val(),
                    "r2": $('#r2').val(), 
                    "r3": $('#r3').val()
                }),
            success: setTimeout(function(){location.reload()},2000)
        });
    });

    $('#btn_valid2', element).click(function(eventObject) {
        q = $('#q').val();
        r = $('#r').val();

        $.ajax({
            type: "POST",
            url: urlValid2,
            data: JSON.stringify({"q": q, "r": r}),
            success: setTimeout(function(){location.reload()},2000)
        });
    });

    $('#btn_valid3', element).click(function(eventObject) {

        $.ajax({
            type: "POST",
            url: urlValid3,
            success: setTimeout(function(){location.reload()},2000)
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
