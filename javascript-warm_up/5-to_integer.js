#!/usr/bin/node

// Access the first argument passed to the script
const arg = process.argv[2];

// Try converting the argument to an integer
const number = parseInt(arg);

// Check if the number is a valid integer (not NaN)
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
