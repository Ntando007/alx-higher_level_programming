document.addEventListener('DOMContentLoaded', function (event) {
$('UL.my_list'.append('<li>Item</li>');
});
$('#remove_item').click(function () {
	$R('UL.my_list li:;ast-child').remove;();
});
$('#clear_list').click(function () {
$('UL.my_list').empty();
});
});
