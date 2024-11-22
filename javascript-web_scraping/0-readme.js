#!/usr/bin/node

/**
 * Script to read and print the content of a file.
 *
 * Usage:
 *   ./0-readme.js <file_path>
 *
 * Arguments:
 *   file_path: The path to the file that should be read.
 *
 * Behavior:
 *   - The script reads the content of the file in UTF-8 encoding.
 *   - If successful, it prints the file's content to the console.
 *   - If an error occurs (e.g., file not found), it prints the error object.
 */

// Import the file system module to handle file operations
const fs = require('fs');

// Retrieve the file path from command-line arguments
const filePath = process.argv[2];

// Check if the file path is provided
if (!filePath) {
  console.error('Error: No file path provided');
  process.exit(1); // Exit the script with an error code
}

// Read the file in UTF-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurs
    console.error(err);
  } else {
    // Print the content of the file if reading is successful
    console.log(data);
  }
});
