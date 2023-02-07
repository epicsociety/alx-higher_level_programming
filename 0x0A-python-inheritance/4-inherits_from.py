#!/usr/bin/python3
"""
module that returns True if the object is an
instance of a class that inherited
(directly or indirectly) from the
specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """function that Returns True or Flase"""
    return (isinstance(obj, a_class) and (type(obj) is not a_class))
