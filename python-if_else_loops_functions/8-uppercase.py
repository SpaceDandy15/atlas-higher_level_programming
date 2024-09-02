#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
