#!/usr/bin/python3
"""Defines a JSON File-reading function"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) a f:
        return json.load(f)
