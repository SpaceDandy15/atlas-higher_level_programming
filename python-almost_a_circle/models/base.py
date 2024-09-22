#!/usr/bin/python3
"""
This module defines the Base class, which serves as a foundational class
for other geometric shapes. It handles the assignment of unique ids
to instances.
"""

import json  # Import the json module
import os  # Import os module for file operations

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
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            dictionary (dict): A dictionary of attributes to set on the instance.

        Returns:
            instance: An instance of Rectangle or Square with attributes set.
        """
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle  # Local import
            dummy_instance = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            from models.square import Square  # Local import
            dummy_instance = Square(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from the JSON file.

        The filename is <Class name>.json. If the file doesn't exist,
        it returns an empty list.

        Returns:
            list: A list of instances of the class.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.isfile(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()
        
        list_dicts = cls.from_json_string(json_string)
        instances = [cls.create(**d) for d in list_dicts]
        return instances
