$('document').ready(function () {
	$('INPUT#btn_translate').click(translate);
	$(INPUT#langauge_code').focus(function () {
		$(this).keydown(function (e) {
			if (e.keyCode === 13) {
				translate();
			}
		});
	});
});
function translate () {
	const url = 'https://www.fourtonfish.com/hellosalut/?';
	$.get(url + $.param({ lang: $("INPUT#langauge_code').val() }), function (data) {
		$('DIV#hello').html(data.hello);
	});
}
