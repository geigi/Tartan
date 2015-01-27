function init() {
	initAlbums();
}

function initAlbums() {
	var albums = ["Roadtrip '13", "Geburtstag Mom April 2012222", "Kitties", "California Love '09", "Urlaub '14", "Amsterdam"]

	for (i = 0; i < albums.length; ++i) {
		addAlbum(albums[i]);
	}

	displayAlbums();
}

function addAlbum(name) {
	container = document.getElementById("main-container");
	var album = document.createElement("div");
	var header = document.createElement("div");
	var content = document.createElement("div");
	var headerText = document.createElement("span");
	var leftColumn = document.createElement("div");
	var rightColumn = document.createElement("div");
	var upperLeft = document.createElement("div");
	var upperRight = document.createElement("div");
	var lowerLeft = document.createElement("div");
	var lowerRight = document.createElement("div");
	var br = document.createElement("br");
	var uploaded = document.createElement("span");
	var a = document.createElement("a");

	a.setAttribute("href", "album.html");

	album.id = name;
	album.className = "panel";

	header.className = "panel-heading";
	
	headerText.className = "panel-heading-text";
	headerText.innerHTML = name;

	uploaded.innerHTML = "uploaded: 16.08.12";

	content.className = "panel-body";

	leftColumn.className = "leftColumn";
	rightColumn.className = "rightColumn";
	upperLeft.className = "preview upperLeft";
	upperRight.className = "preview upperRight";
	lowerLeft.className = "preview lowerLeft";
	lowerRight.className = "preview lowerRight";

	leftColumn.appendChild(upperLeft);
	leftColumn.appendChild(upperRight);
	rightColumn.appendChild(lowerLeft);
	rightColumn.appendChild(lowerRight);

	content.appendChild(leftColumn);
	content.appendChild(rightColumn);
	header.appendChild(headerText);
	header.appendChild(br);
	header.appendChild(uploaded);
	album.appendChild(content);
	album.appendChild(header);
	a.appendChild(album);
	container.appendChild(a);
}

function displayAlbums() {
	$(function() {
		$(".panel").fadeToggle(0).fadeToggle(300);
	}); 
}