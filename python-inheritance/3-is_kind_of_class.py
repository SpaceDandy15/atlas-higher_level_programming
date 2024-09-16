#!/usr/bin/python3
"""Defines a class and inherited class-checking funciton."""


def is_kind_ofclass(obj,a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to mathc the type of obj to.
    Returns:
        If obj is an instance or inherited instanceof a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False