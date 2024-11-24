$(document).ready(function() {
    // Make an AJAX GET request to the Star Wars API
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
      // Display the name of the character in the DIV#character
      $('#character').text(data.name);
    });
  });
  