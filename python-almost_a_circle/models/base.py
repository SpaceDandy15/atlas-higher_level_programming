#!/usr/bin/python3
"""
This module defines the Base class, which serves as a foundational class
for other geometric shapes. It handles the assignment of unique ids
to instances.
"""

import json  # Import the json module

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of the list_dictionaries.
                 If list_dictionaries is None or empty, returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)  # Convert the list to a JSON string
