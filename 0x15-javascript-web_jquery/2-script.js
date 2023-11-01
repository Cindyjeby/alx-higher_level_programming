$(document).ready(function() {
	//select div by id
	const redHeaderDiv = $('DIV#red_header');
	//event handler
	redHeaderDiv.click(function() {
		const headerElement = $('header');
		if (headerElement) {
			headerElement.css('color', '#FF0000');
		} else {
			console.error('header element not found');
		}
	});
});
