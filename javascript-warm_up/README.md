JavaScript Basics - Learning Summary
Introduction
This README provides a summary of the key concepts we've covered in JavaScript so far. From basic syntax to more advanced features, we've explored how to work with variables, arguments, loops, functions, and more.

Table of Contents
Shebang (#!/usr/bin/node)
Working with process.argv and Command-Line Arguments
Variables and Constants (const, let, and var)
Conditionals (if/else)
Loops (for and while)
Functions and Returning Values
Basic Array Operations
Validating Input and Converting Types
1. Shebang (#!/usr/bin/node)
The shebang line (#!/usr/bin/node) at the beginning of a script tells the system to use Node.js to execute the script.
It ensures that the script is run with the correct interpreter when executed from the command line.
2. Working with process.argv and Command-Line Arguments
process.argv: This is an array that holds all command-line arguments passed to the Node.js script when it is run.
process.argv[0]: Path to Node.js executable
process.argv[1]: Path to the script file
process.argv[2] and onwards: User-provided arguments
Example:
js
Copy code
const arg = process.argv[2]; // Accesses the first user argument
process.argv.length - 2: This is used to get the count of arguments passed by the user (excluding the script execution path).
3. Variables and Constants (const, let, and var)
const: Defines a constant value that cannot be reassigned. Typically used for values that should remain unchanged.
Example:
js
Copy code
const pi = 3.14; 
let: Defines a variable whose value can be reassigned. It is block-scoped.
Example:
js
Copy code
let age = 30;
age = 31; // Reassigned
var: An older keyword that also defines a variable, but it is function-scoped instead of block-scoped. It is less commonly used now in modern JavaScript.
4. Conditionals (if, else if, and else)
The if statement is used to execute a block of code based on a condition being true.
else if and else provide alternative conditions and blocks of code to execute if the initial if condition is false.
Example:
js
Copy code
if (arg === undefined) {
  console.log('No argument');
} else if (arg === 'Hello') {
  console.log('Hello argument!');
} else {
  console.log('Other argument');
}
5. Loops (for and while)
for loop: Used for iterating through a range of values or elements in an array.
Example:
js
Copy code
for (let i = 0; i < 5; i++) {
  console.log(i); // Outputs numbers 0 to 4
}
while loop: Executes a block of code as long as a specified condition is true.
Example:
js
Copy code
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}
6. Functions and Returning Values
Function Definition: Functions are used to group reusable blocks of code. They can take input (parameters) and return output (results).
Example:
js
Copy code
function add(a, b) {
  return a + b;
}
console.log(add(3, 4)); // Outputs 7
7. Basic Array Operations
Creating and Accessing Arrays: Arrays hold multiple elements and can be accessed using their index.
Example:
js
Copy code
const languages = ["C", "Python", "JavaScript"];
console.log(languages[0]); // Outputs "C"
Iterating through Arrays: You can use loops like for to access each element in an array.
Example:
js
Copy code
const languages = ["C", "Python", "JavaScript"];
for (let i = 0; i < languages.length; i++) {
  console.log(languages[i]);
}
8. Validating Input and Converting Types
Validating Input: You can check if input is valid using functions like isNaN() or conditional checks.

Example:
js
Copy code
const number = parseInt(arg);
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
Converting Input: Use functions like parseInt() to convert strings to numbers or String() to convert values to strings.