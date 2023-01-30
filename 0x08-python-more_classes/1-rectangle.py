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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        self.__width = width

    @width.setter
    def width(self, value):
        self.__width = value

        if value != int:
            raise TypeError ('width must be an integer')
        if value < 0:
            raise ValueError ('width must be >= 0')

    @property
    def height(self):
        self.__height = height

    @height.setter
    def height(self, value):
        self.__height = value

        if value != int:
            raise TypeError ('width must be an integer')
        if value < 0:
            raise ValueError ('width must be >= 0')
