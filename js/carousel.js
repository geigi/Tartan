curPic = 0;

$(window).resize(function(){
    resizeImg();
});

function init() {
  document.onkeydown = checkKey;
  initImg();
}

function initImg() {
  picName = getGet('img');
  curPic = picName;
  img = document.getElementById("fullPic");
  img.src = "sample/" + picName + ".jpg";
}

function resizeImg() {
  var height = parseInt($(window).height()) - 200;

  $('.fullPic').css({
    'max-width': $(window).width(),
    'max-height': height,
  });

  $('.container').css({
    'width': $('.fullPic').width(),
  })
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

function prev() {
  window.location = "carousel.html?img=" + (curPic - 1);
}

function next() {
  window.location = "carousel.html?img=" + (parseInt(curPic) + 1);
}

function imgLoaded() {
  img = document.getElementById("fullPic");
  if (img.height > 0)
  {
    resizeImg();
    loader = document.getElementById("loader");

    loader.style.display = "none";
    $(".fullPic").fadeIn();
  }
}

function checkKey(e) {
    e = e || window.event;

    if (e.keyCode == '37' || e.keyCode == '8') {
       // left arrow
       prev();
    }
    else if (e.keyCode == '39' || e.keyCode == '32' || e.keyCode == '13') {
       // right arrow
       next();
    }
}

function hide(elem) {
  sender = document.getElementById(elem);
  sender.style.visibility = "hidden";
}

function show(elem) {
  sender = document.getElementById(elem);
  sender.style.visibility = "visible";
}