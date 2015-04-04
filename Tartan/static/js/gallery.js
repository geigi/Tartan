function init() {
	initDropdown();
	initSearch();
}

function initSearch() {
	$("#search").bind("paste cut keydown",function(e) {
        var that = this;
        setTimeout(function() {
                search($(that).val());
            },100);
    });
}

function search(search) {
	var albums = document.getElementsByClassName("panel-heading-text");
	
	for (i = 0; i < albums.length; ++i) {
		var title = albums[i].firstChild.data.toLowerCase();
		var album = albums[i].parentNode.parentNode.parentNode;

		if (title.indexOf(search.toLowerCase()) > -1) {
			album.setAttribute("style", "display: inline-block;")
		}
		else {
			album.setAttribute("style", "display: none;")
		}
	}
}