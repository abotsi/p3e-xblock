/* Javascript for P3eXBlock. */
function P3eXBlock(runtime, element) {

    function okay(result) {
        alert("success!\nresult="+result.val)
    }

    var urlValid1 = runtime.handlerUrl(element, 'validate_phase1');
    var urlValid2 = runtime.handlerUrl(element, 'validate_phase2');
    var urlValid3 = runtime.handlerUrl(element, 'validate_phase3');

    $('#btn_valid1', element).click(function(eventObject) {
        eventObject.preventDefault();
        r1 = $('#r1').val();
        r2 = $('#r2').val();
        r3 = $('#r3').val();

        $.ajax({
            type: "POST",
            url: urlValid1,
            data: JSON.stringify({"r1": r1, "r2": r2, "r3": r3}),
            success: setTimeout(function(){location.reload()},2000)
        });
    });

    $('#btn_valid2', element).click(function(eventObject) {
        eventObject.preventDefault();
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
        eventObject.preventDefault();

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
