var time = 2500;

var curPic = 0;
var dia = 0;
var timer;
var pDic;
var inversepDic
var loaded = false;

$(window).resize(function(){
    resizeImg();
});

function init() {
  initDropdown();
  initOverlay();
  createPickerArray();
  document.onkeydown = checkKey;
  initDiashow();
  initPicker();
  initBackButton();
}

function resizeImg() {
  var height = parseInt($(window).height()) - 150;
  var width = parseInt($(window).width()) - 200;

  $('.fullPic').css({
    'max-width': width,
    'max-height': height,
  }); 

  $('.container').css({
    'width': $('.fullPic').width(),
  })
}

function prev() {
  ChangeImage(false);

  setPickerPosition(currentId);
  var pos = pDic[currentId];
  var oldPic = getKeyFromDic(pDic, pos + 1);
  activePicker(false,  oldPic);

  refreshPicker();
}

function next() {
  ChangeImage(true);

  setPickerPosition(currentId);
  var pos = pDic[currentId];
  var oldPic = getKeyFromDic(pDic, pos - 1);
  activePicker(false, oldPic);

  refreshPicker();
}

function imgLoaded() {
  img = document.getElementById("fullPic");
  if (img.height > 0) {
    resizeImg();
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

  setPickerPosition(currentId);

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
  var pane = $('.picker');
  var api = pane.data('jsp');
  api.scrollToY((pDic[pic_name] - 2) * 65);

  activePicker(true, pic_name);
}

function activePicker(active, pic_id) {
  var picker_prev = document.getElementById("thumb" + pic_id);
  if (active) {
    picker_prev.className = "";
  }
  else {
    picker_prev.className = "inactive";
  }
}

function createPickerArray() {
  pDic = {};
  var thumbs = document.getElementById("picker").children;

  for (i = 0; i < thumbs.length; i++) {
    pDic[thumbs[i].id.substring(5)] = i;
  }
}

function getKeyFromDic(dic, val) {
  for (var key in dic) {
    if (dic[key] == val) {
      return key;
    }
  }

  return null;
}

function initOverlay() {
  hide("nav-left");
  hide("nav-right");
}

function initBackButton() {
  // Safari bug fix
  window.addEventListener('load', function() {
      setTimeout(function() {
        loaded = true;
      }, 0);
  });

  $(window).on("popstate", function (e) {
    if (loaded) {
      location.reload()
    }
  });
}