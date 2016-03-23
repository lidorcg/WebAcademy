$(document).ready(function () {
    $('.ajax-form').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            type: $(this).attr("method"),
            url: $(this).attr("action"),
            data: $(this).serialize()
        });
        return false;
    });
});