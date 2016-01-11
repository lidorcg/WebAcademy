$(document).ready(function () {
    $('#add-tag').click(function () {
        var name = this.form.elements["name"].value;
        var tag = $('<span class="tag btn btn-default"></span>').text(name);
        $('#all-tags').append(tag);
    });
});
// ToDo use ajax and success func to add tags
// ToDo reset form after submit
// ToDo add form validations