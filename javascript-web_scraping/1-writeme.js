#!/usr/bin/node

/**
 * Script to write a string to a file.
 *
 * Usage:
 *   ./1-writeme.js <file_path> <string_to_write>
 *
 * Arguments:
 *   file_path: The path to the file where the string will be written.
 *   string_to_write: The string to be written to the file.
 *
 * Behavior:
 *   - The script writes the string to the file in UTF-8 encoding.
 *   - If successful, the file will contain the provided string.
 *   - If an error occurs during writing, it prints the error object.
 */

// Import the file system module to handle file operations
const fs = require('fs');

// Retrieve command-line arguments for file path and string to write
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Check if both arguments are provided
if (!filePath || !stringToWrite) {
  console.error('Error: Missing arguments. Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1); // Exit the script with an error code
}

// Write the string to the file in UTF-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurs
    console.error(err);
  }
});
