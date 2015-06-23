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

function initDropdown() {
  ordering = getGet('ordering');
  dropdown = document.getElementById("ordering");

  if (ordering === undefined) {
    dropdown.options[0].selected = true;
    return;
  }

  switch(ordering) {
    case 'name':
      dropdown.options[2].selected = true;
      break;
    case 'namereverse':
      dropdown.options[3].selected = true;
      break;
    case 'oldest':
      dropdown.options[1].selected = true;
      break;
    case 'newest':
      dropdown.options[0].selected = true;
      break;
    case 'newestphotofirst':
      dropdown.options[4].selected = true;
      break;
    case 'newestphotolast':
      dropdown.options[5].selected = true;
      break;
  }
}