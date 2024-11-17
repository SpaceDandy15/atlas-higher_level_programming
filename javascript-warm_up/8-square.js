#!/usr/bin/node

// Parse the first argument as an integer
const size = parseInt(process.argv[2]);

// Check if size is a valid number
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // Use a loop to print the square
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
