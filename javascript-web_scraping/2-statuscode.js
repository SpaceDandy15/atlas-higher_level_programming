#!/usr/bin/node

/**
 * Script to display the status code of a GET request.
 *
 * Usage:
 *   ./2-statuscode.js <URL>
 *
 * Arguments:
 *   URL: The URL to send the GET request to.
 *
 * Behavior:
 *   - Makes a GET request to the specified URL.
 *   - Prints the status code of the response in the format: "code: <status code>".
 *   - Uses the 'request' module.
 */

// Import the request module
const request = require('request');

// Retrieve the URL from command-line arguments
const url = process.argv[2];

// Check if the URL is provided
if (!url) {
  console.error('Error: Missing URL. Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Make a GET request to the URL
request.get(url, (error, response) => {
  if (error) {
    // Print the error object if an error occurs
    console.error(error);
  } else {
    // Print the status code of the response
    console.log(`code: ${response.statusCode}`);
  }
});
