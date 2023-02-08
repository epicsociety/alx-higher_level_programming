#!/usr/bin/python3
""" MyInt class"""


class MyInt(int):
    """rebel version"""

    def __new__(cls, *args, **kwargs):
        """creates a new instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """!= interchanged with =="""
        return int(self) != other

    def __ne__(self, other):
        """== interchanged with !="""
        return int(self) == other
