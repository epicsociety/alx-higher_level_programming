#!/usr/bin/python3
"""defines a class"""


class Rectangle:
    """
    an empty Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        instantiation with height and weight
        height: height of rectangle
        width: width of rectagle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width a private atrribute"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height, a private attribute"""

        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
