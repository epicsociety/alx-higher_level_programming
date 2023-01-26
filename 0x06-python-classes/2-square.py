#!/usr/bin/python3
""" Defines a class Square"""


class Square:
    """A class square"""

    def __init__(self, size=0):
        """
        Args:
        Size: size of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an interger')
