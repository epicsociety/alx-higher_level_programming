#!/usr/bin/python3
"""defines a square"""


class Square:
    """square with private attribute size"""

    def __init__(self, size=0):
        """
        initializes square
        Args:
        size: size of side of square
        """
        self.size = size

    def area(self):
        """finds the area of the square"
        Returns:
            the area of the square
        """
        return (self.size) ** 2

    @property
    def size(self):
        """getter of _size
        Returns:
        The size of the square
        """
        return self.__size

    @size.setter
    def size(sel, value):
        """setter of __size
        Args: the size of the square"
        Returns:
            None
        """
        if type(valuei) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
