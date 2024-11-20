#!/usr/bin/node
/**
 * Prints the number of arguments already printed and the current argument value.
 * Maintains a count of the arguments printed so far.
 * @param {any} item - The argument to log.
 */
exports.logMe = (function () {
    let count = 0; // Closure variable to keep track of printed arguments
    return function (item) {
      console.log(`${count}: ${item}`);
      count++;
    };
  })();
  