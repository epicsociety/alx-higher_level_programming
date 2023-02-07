#!/usr/bin/python3
"""Module for BaseGeometry"""


class BaseGeometry(object):
    """geometry base class"""
    def area(self):
        """implements area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if (value.__class__ is not int):
            raise TypeError("{:} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:} must be greater than 0".format(name))
