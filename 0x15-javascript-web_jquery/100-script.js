document.addEventListener('DOMContentLoader', function () {
	const headerElement = document.querySelector('header');

	if (headerElement) {
		headerElement.style.color = '#FF0000';
	} else {
		console.error('header element not found,');
	}
});
