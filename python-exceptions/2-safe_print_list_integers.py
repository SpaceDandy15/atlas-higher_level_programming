#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a lsit that are integers.

    args:
    my_list (list): the list to print elements from.
    x (int): The number of elemetns of my_list to print.

    Returns:
    The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
             continue
    print("")
    return (ret)
