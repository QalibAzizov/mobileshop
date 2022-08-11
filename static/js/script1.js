// Get the container element
var btnContainer = document.getElementById("myDIV");

// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByClassName("btt");

// Loop through the buttons and add the active class to the current/clicked button
$(function($) {
    let url = window.location.href;
    $('li a').each(function() {
      if (this.href === url) {
        $(this).closest('li').addClass('active');
      }
    });
  });
