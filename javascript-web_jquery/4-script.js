// Wait for the document to be ready
$(document).ready(function() {
    // Bind a click event handler to the element with id "toggle_header"
    $('#toggle_header').click(function() {
      // Toggle between "red" and "green" classes on the <header> element
      $('header').toggleClass('red green');
    });
  });
  