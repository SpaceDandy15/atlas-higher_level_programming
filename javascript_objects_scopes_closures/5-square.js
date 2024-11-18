#!/usr/bin/node
/**
 * Square - A class that defines a square and inherits from Rectangle.
 * @class
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  /**
   * Creates an instance of Square.
   * @param {number} size - The size of the square's sides.
   */
  constructor(size) {
    super(size, size); // Call the constructor of Rectangle with width and height as size
  }
}

module.exports = Square;
