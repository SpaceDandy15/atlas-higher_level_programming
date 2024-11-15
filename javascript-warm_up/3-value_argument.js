#!/usr/bin/node

// Get the first argument (if any)
const firstArg = process.argv[2];

// Check if an argument was provided and print the appropriate message
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
