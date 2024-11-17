#!/usr/bin/node
/**
 * Rectangle - A class that defines a rectangle.
 * @class
 */
class Rectangle {
    /**
     * Creates an instance of Rectangle.
     * If w or h is not a positive integer, creates an empty object.
     * @param {number} w - The width of the rectangle.
     * @param {number} h - The height of the rectangle.
     */
    constructor(w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    /**
     * Prints the rectangle using the character 'X'.
     */
    print() {
      if (this.width && this.height) {
        for (let i = 0; i < this.height; i++) {
          console.log('X'.repeat(this.width));
        }
      }
    }
  }
  
  module.exports = Rectangle;
  