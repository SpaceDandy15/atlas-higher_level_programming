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
  }
  
  module.exports = Rectangle;
  