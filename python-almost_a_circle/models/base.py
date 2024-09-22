#!/usr/bin/python3
"""
This module defines the Base class, which serves as a foundational class
for other geometric shapes. It handles the assignment of unique ids
to instances.
"""

class Base:
    """
    The Base class provides a unique identifier for each instance.
    If no id is provided, the class assigns an incremental id automatically.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base instance.

        Args:
            id (int): An optional id for the instance. If not provided,
                      a unique id is generated based on the number of objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
