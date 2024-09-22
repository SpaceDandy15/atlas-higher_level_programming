#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
The Square class models a square with a size and coordinates (x, y).
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class represents a geometric square, inheriting from the Rectangle class.
    It has a private attribute for size and uses the attributes of Rectangle for x and y.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): Optional id, inherited from Base.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square, with validation."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes using *args or **kwargs.

        Args:
            args (tuple): A variable number of positional arguments in the order of
                          (id, size, x, y).
            kwargs (dict): A dictionary of key/value pairs representing attributes.
        """
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.size = args[1] if len(args) > 1 else self.size
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square instance.

        Returns:
            dict: A dictionary containing the attributes of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Format:
        [Square] (<id>) <x>/<y> - <size>

        Returns:
            str: The formatted string representing the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
