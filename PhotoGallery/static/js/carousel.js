var curPic = 0;
var dia = 0;
var timer;
var time = 2500;

$(window).resize(function(){
    resizeImg();
});

function init() {
  document.onkeydown = checkKey;
  initDiashow();
  initPicker();
}

function resizeImg() {
  var height = parseInt($(window).height()) - 150;

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
  ChangeImage(false);
}

function next() {
  ChangeImage(true);
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

function initDiashow() {
  getDia = getGet('dia');
  if (getDia == '1') {
    button = document.getElementById("play");
    button.className = "fa fa-fw fa-pause fa-lg";
    dia = 1;
    timer = setInterval(function() {next()}, time);
  }
  else {
    dia = 0;
  }
}

function diashow() {
  if (dia == 0) {
    dia = 1;
    button = document.getElementById("play");
    button.className = "fa fa-fw fa-pause fa-lg";

    timer = setInterval(function() {next()}, time);
  }
  else {
    dia = 0;
    button = document.getElementById("play");
    button.className = "fa fa-fw fa-play fa-lg";

    window.clearInterval(timer);
  }
}

function initPicker() {
  $('.picker').jScrollPane({
    showArrows: true,
    animateScroll: true,
    arrowScrollOnHover: true
  });
}