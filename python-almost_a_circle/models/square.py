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

    @property
    def size(self):
        """Gets the size of the square (width or height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square, with validation for width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.

        Args:
            *args: A list of non-keyworded arguments:
                1st argument: id
                2nd argument: size
                3rd argument: x
                4th argument: y
            **kwargs: A dictionary of keyworded arguments to update attributes.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Format:
        [Square] (<id>) <x>/<y> - <size>

        Returns:
            str: The formatted string representing the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
