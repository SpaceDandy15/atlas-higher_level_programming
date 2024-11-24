#!/usr/bin/node
/**
 * Script to count and print the number of movies where the character "Wedge Antilles" appears.
 * 
 * Usage: ./4-starwars_count.js <API_URL>
 * 
 * Requirements:
 * - The first argument is the API URL of the Star Wars API.
 * - Character ID 18 is used to filter the results.
 * - Uses the `request` module to perform the API call.
 */

const request = require('request'); // Import the request module to handle HTTP requests

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Validate that the API URL was provided
if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

// Perform the HTTP GET request
request(apiUrl, (error, response, body) => {
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

    // Character ID for "Wedge Antilles"
    const wedgeId = '18';

    // Count the number of movies containing the character
    const count = data.results.filter((film) =>
      film.characters.some((characterUrl) => characterUrl.includes(`/${wedgeId}/`))
    ).length;

    // Print the count
    console.log(count);
  } catch (parseError) {
    // Handle errors during JSON parsing
    console.error('Error parsing JSON:', parseError.message);
  }
});
