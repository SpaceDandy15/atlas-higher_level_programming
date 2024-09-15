#!/usr/bin/python3
"""Defines and object attribute look up function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
