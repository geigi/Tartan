function init() {
	initDropdown();
}

function displayAlbums() {
	$(function() {
		$(".panel").fadeToggle(0).fadeToggle(300);
	}); 
}

function initDropdown() {
	ordering = getGet('ordering');
	dropdown = document.getElementById("ordering");

	switch(ordering) {
		case 'name':
			dropdown.options[0].selected = true;
			break;
		case 'namereverse':
			dropdown.options[1].selected = true;
			break;
		case 'newest':
			dropdown.options[2].selected = true;
			break;
		case 'oldest':
			dropdown.options[3].selected = true;
			break;
	}
}