#!/usr/bin/node

// Retrieve arguments and convert them to integers
const args = process.argv.slice(2).map(Number);

// Check conditions for no arguments or one argument
if (args.length <= 1) {
  console.log(0);
} else {
  // Sort arguments in descending order and get the second biggest
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
