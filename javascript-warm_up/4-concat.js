#!/usr/bin/node

// Access arguments passed to the script
const args = process.argv.slice(2);

// Get the first and second arguments or default to "undefined"
const arg1 = args[0] || 'undefined';
const arg2 = args[1] || 'undefined';

// Print the formatted output
console.log(`${arg1} is ${arg2}`);
