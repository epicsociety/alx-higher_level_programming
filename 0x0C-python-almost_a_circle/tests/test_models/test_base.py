#!/usr/bin/python3
"""a base class"""


class Base:
    """the definition of the base class"""
    __nb_objects = 0  #private class attribute

    def __init__(self, id=None):
        """instantiation of the base class"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
