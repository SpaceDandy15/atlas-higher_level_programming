#!/usr/bin/node

// Function to compute factorial recursively
function factorial(n) {
    if (n <= 1) {
      return 1;
    }
    return n * factorial(n - 1);
  }
  
  // Parse the argument as an integer
  const num = parseInt(process.argv[2]);
  
  // Compute and print the factorial
  console.log(factorial(isNaN(num) ? 1 : num));
  