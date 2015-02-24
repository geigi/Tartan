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

  var img = document.getElementsByClassName("fullPic")[0];
  setPickerPosition(img.id);
  activePicker(false, parseInt(img.id) + 1);

  refreshPicker();
}

function next() {
  ChangeImage(true);

  var img = document.getElementsByClassName("fullPic")[0];
  setPickerPosition(img.id);
  activePicker(false, parseInt(img.id) - 1);

  refreshPicker();
}

function imgLoaded() {
  img = document.getElementsByClassName("fullPic")[0];
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
    animateScroll: false,
    arrowScrollOnHover: true
  });

  $('.picker').each(
    function() {
      var api = $(this).data('jsp');
      var throttleTimeout;
      $(window).bind('resize',
        function() {
          if (!throttleTimeout) {
            throttleTimeout = setTimeout(
              function() {
                api.reinitialise();
                throttleTimeout = null;
              },
              50
            );
          }
        }
      );
  });

  var img = document.getElementsByClassName("fullPic")[0];
  setPickerPosition(img.id);

  refreshPicker();
}

function refreshPicker() {
  $('.picker').each(
    function() {
      var api = $(this).data('jsp');
      var throttleTimeout;
      if (!throttleTimeout) {
        throttleTimeout = setTimeout(
          function() {
            api.reinitialise();
            throttleTimeout = null;
          },
          50
        );
      }
  });
}

function setPickerPosition(pic_name) {
  // var thumbs = document.getElementById("picker").childNodes;
  // var position = 0;
  // for (i=0; i<thumbs.length; i++) {
  //   position++;
  //   var img = thumbs[i].id;

  //   if (img == pic_name) {
  //     break;
  //   }
  // }

  var pane = $('.picker');
  var api = pane.data('jsp');
  api.scrollToY((parseInt(pic_name) - 1) * 50);

  activePicker(true, pic_name);
}

function activePicker(active, pic_id) {
  var picker_prev = document.getElementById("thumb" + pic_id);
  if active {
    picker_prev.className = "";
  }
  else {
    picker_prev.className = "inactive";
  }
}