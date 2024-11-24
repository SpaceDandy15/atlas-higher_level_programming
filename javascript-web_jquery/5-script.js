// Wait for the document to be ready
$(document).ready(function() {
    // Bind a click event handler to the element with id "add_item"
    $('#add_item').click(function() {
      // Append a new <li> element to the <ul> with class "my_list"
      $('ul.my_list').append('<li>Item</li>');
    });
  });
  