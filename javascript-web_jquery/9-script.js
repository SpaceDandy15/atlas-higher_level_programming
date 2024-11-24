$(document).ready(function() {
    // Fetch the translation from the API
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
      // Update the #hello element with the translated "hello"
      $('#hello').text(data.hello);
    });
  });
  