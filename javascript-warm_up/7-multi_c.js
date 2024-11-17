#!/usr/bin/node

// Retrieve the first argument passed
const arg = process.argv[2];

// Parse the argument to an integer
const x = parseInt(arg);
// check if x is not a valid number
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
