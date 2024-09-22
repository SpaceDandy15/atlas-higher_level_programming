#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from Base.
The Rectangle class models a rectangle with width, height, and coordinates (x, y).
"""

from models.base import Base

class Rectangle(Base):
    """
    The Rectangle class represents a geometric rectangle, inheriting from the Base class.
    It has private attributes for width, height, and coordinates (x, y), along with
    public getters and setters for each.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle.
            y (int): The y coordinate of the rectangle.
            id (int): Optional id, inherited from Base.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for width
    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, with validation."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, with validation."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        """Gets the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate of the rectangle, with validation."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        """Gets the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate of the rectangle, with validation."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle instance.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance using the '#' character, considering x and y.

        This method prints empty lines for y and shifts the rectangle for x.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>

        Returns:
            str: The formatted string representing the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes using *args or **kwargs.

        Args:
            args (tuple): A variable number of positional arguments in the order of
                          (id, width, height, x, y).
            kwargs (dict): A dictionary of key/value pairs representing attributes.
        """
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.width = args[1] if len(args) > 1 else self.width
            self.height = args[2] if len(args) > 2 else self.height
            self.x = args[3] if len(args) > 3 else self.x
            self.y = args[4] if len(args) > 4 else self.y
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle instance.

        Returns:
            dict: A dictionary containing the attributes of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
