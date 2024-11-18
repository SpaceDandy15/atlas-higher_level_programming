#!/usr/bin/node
/**
 * Square - A class that defines a square and inherits from Square of 5-square.js.
 * @class
 */
const SquareBase = require('./5-square');

class Square extends SquareBase {
  /**
   * Prints the square using the character c.
   * If c is undefined, prints using the character 'X'.
   * @param {string} c - The character to print the square with.
   */
  charPrint(c) {
    const char = c || 'X'; // Default to 'X' if c is undefined
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
