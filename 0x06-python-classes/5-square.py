#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initializes size of the square
        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """size of Square class"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size of Square class"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints square with # character
        """
        if self.__size == 0:
            print()
        else:
            integer = 0
            while integer < self.__size:
                print("{}".format("#"), end="")
                num += 1
            print()
            integer += 1
