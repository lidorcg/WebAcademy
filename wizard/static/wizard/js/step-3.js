$(document).ready(function () {
    $('.group').each(function () {
        $(this).sortable({
            connectWith: ['.group'],
            receive: function (event, ui) {
                var group_id = this.getAttribute("data-group-id");
                var data = {group: group_id};
                var concept_id = ui.item.context.getAttribute("data-concept-id");
                $.post('/wizard/concepts/' + concept_id + '/update/', data);
            }
        });
    });
});