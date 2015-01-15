function init() {
	initAlbums();
}

function initAlbums() {
	for (i = 1; i < 21; ++i) {
		addAlbum(i);
	}

	displayAlbums();
}

function addAlbum(name) {
	container = document.getElementById("main-container");
	var pic = document.createElement("div");
	var content = document.createElement("div");
	var img = document.createElement("img");
	var a = document.createElement("a");

	a.setAttribute("href", "carousel.html?img=" + name);

	pic.id = name;
	pic.className = "panel pic-preview";

	content.className = "panel-body panel-body-preview";

	img.setAttribute("src", "sample/" + name + ".jpg");
	img.className = "image-preview";

	content.appendChild(img);
	pic.appendChild(content);
	a.appendChild(pic);
	container.appendChild(a);
}

function displayAlbums() {
	$(function() {
		$(".panel").fadeToggle(0).fadeToggle(300);
	}); 
}