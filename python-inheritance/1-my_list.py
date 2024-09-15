#!/usr/bin/python3


class MyList(list):
    """a subclass of list"""
    def __init__(self_):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
