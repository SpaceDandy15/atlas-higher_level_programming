#!/usr/bin/node
/**
 * Script to fetch and print the title of a Star Wars movie given its episode number.
 * 
 * Usage: ./3-starwars_title.js <movieId>
 * 
 * The script uses the Star Wars API with the endpoint:
 * https://swapi-api.hbtn.io/api/films/:id
 * 
 * Requirements:
 * - The first argument is the movie ID (episode number).
 * - Uses the `request` module to perform the API call.
 */

const request = require('request'); // Import the request module to handle HTTP requests

// Get the movie ID (episode number) from the command-line arguments
const movieId = process.argv[2];

// Validate that the movie ID was provided
if (!movieId) {
  console.error('Usage: ./3-starwars_title.js <movieId>');
  process.exit(1);
}

// Construct the API URL using the provided movie ID
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Perform the HTTP GET request
request(url, (error, response, body) => {
  // Handle errors during the HTTP request
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Handle non-200 HTTP responses
  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    return;
  }

  try {
    // Parse the JSON response body
    const data = JSON.parse(body);

    // Print the title of the movie
    console.log(data.title);
  } catch (parseError) {
    // Handle errors during JSON parsing
    console.error('Error parsing JSON:', parseError.message);
  }
});
