#!/usr/bin/python3
"""
The "0-add_integer" module.
has one function that adds two integers
"""


def add_integer(a, b=98):
    """method adds integers
    Return the sum
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    return a + b
