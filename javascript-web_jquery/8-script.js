$(document).ready(function() {
    // Make an AJAX GET request to fetch movie data
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
      // Iterate over the films and append their titles to the UL#list_movies
      data.results.forEach(function(movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    });
  });
  