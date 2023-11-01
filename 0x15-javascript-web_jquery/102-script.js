$(document).ready(function() {
	$('#btn_traslate').click(function() {
		const languageCode = $('#language_code').val();

		$.ajax({
			url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=${langaugeCode}',
			method: 'GET',
			dataType: 'json',
			success: function (data) {
				$('#hello').text(translation);
			},
			error: function () {
				$('#hello').text('Translation not found.');
			}
		});
	});
});
