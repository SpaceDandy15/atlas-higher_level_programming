#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    a function that prints a dictionary by ordered keys
    """
    keys = list(a_dictionary.key())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
