#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
The Square class models a square with a size and coordinates (x, y).
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class represents a geometric square, inheriting from the Rectangle class.
    It has private attributes for size (width and height) and coordinates (x, y).
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): Optional id, inherited from Rectangle.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Format:
        [Square] (<id>) <x>/<y> - <size>

        Returns:
            str: The formatted string representing the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
