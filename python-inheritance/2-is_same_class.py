#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (any): The class to match the type of obj to.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    if type(obj) is a_class:
        return True
    return False