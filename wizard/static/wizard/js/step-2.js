$(document).ready(function () {
    $('#add-tag').click(function () {
        var name = this.form.elements["name"].value;
        var tag = $('<span class="tag btn btn-default"></span>').text(name);
        $('.all-tags').append(tag);
    });

    $('#go-to-3').on('click', function (event) {
        $('.nav-pills a[href="#step-3"]').tab('show');
    });
});
// ToDo reset form after submit
// ToDo add form validations