#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".fomrat().

    Args:
    value (int): the integer to print.

    Returns:
    if a typeerror or value error occurs -false.
    Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    execpt (TypeError, ValueError):
        return (False)
