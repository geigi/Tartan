function init() {
	initDropdown();
	initSearch();
}

function initDropdown() {
	ordering = getGet('ordering');
	dropdown = document.getElementById("ordering");

	if (ordering === undefined) {
		dropdown.options[2].selected = true;
		return;
	}

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

function initSearch() {
	$("#search").bind("paste cut keydown",function(e) {
        var that = this;
        setTimeout(function() {
                search($(that).val());
            },100);
    });
}

function getGet(index) {
  var $_GET = {};
  if(document.location.toString().indexOf('?') !== -1) {
      var query = document.location
                     .toString()
                     // get the query string
                     .replace(/^.*?\?/, '')
                     // and remove any existing hash string (thanks, @vrijdenker)
                     .replace(/#.*$/, '')
                     .split('&');

      for(var i=0, l=query.length; i<l; i++) {
         var aux = decodeURIComponent(query[i]).split('=');
         $_GET[aux[0]] = aux[1];
      }
  }
  //get the 'index' query parameter
  return $_GET[index];
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