#!/usr/bin/node
/**
 * Script that fetches the content of a webpage and stores it in a file.
 *
 * Usage:
 *   ./5-request_store.js <URL> <file_path>
 *
 * Arguments:
 *   <URL>: The URL of the webpage to fetch.
 *   <file_path>: The file path where the response body will be saved.
 *
 * The file will be UTF-8 encoded. The script uses the `request` module for HTTP requests
 * and the `fs` module for file operations.
 */

// Import required modules
const request = require('request'); // For making HTTP requests
const fs = require('fs'); // For file system operations

// Get command-line arguments
const url = process.argv[2]; // The URL to fetch
const filePath = process.argv[3]; // The file path to save the response

// Validate arguments
if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

/**
 * Fetches the webpage content and writes it to a file.
 */
request(url, (error, response, body) => {
  if (error) {
    // Log and exit if there's an error with the HTTP request
    console.error('Error fetching the URL:', error.message);
    return;
  }

  // Write the response body to the specified file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      // Log and exit if there's an error writing to the file
      console.error('Error writing to file:', err.message);
    } else {
      // Success message (optional)
      console.log(`Content successfully saved to ${filePath}`);
    }
  });
});
