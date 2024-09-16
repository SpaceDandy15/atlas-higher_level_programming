#!/usr/bin/python3
"""
This module contains the MyList class, which is a subclass of the built-in list class.
It includes methods for appending elements and printing a sorted version of the list.
"""

class MyList(list):
    """a subclass of list"""
    def __init__(self_):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))