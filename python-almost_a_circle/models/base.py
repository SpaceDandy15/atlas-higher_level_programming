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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = f"{cls.__name__}.json"  # Create the filename based on class name
        if list_objs is None:
            list_objs = []
        
        # Convert the list of objects to a list of dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        # Write the JSON string to the file
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string. Returns an empty list
                  if json_string is None or empty.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)  # Convert the JSON string back to a list
