#!/usr/bin/python3
"""Module that adds two integers"""


def add_integer(a, b=98):
    """ add_integer method
    Args:
    a, b - ints
    Raises:
    TypeError: if a or b is not an int
    Returns:
    Integer: sum of a and b
    """
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return a + b
