#!/usr/bin/python3
""" A class module"""


class Square:
    """defines the class square """

    def __init__(self, size=0, position=(0, 0)):
        """
        initializes the class square
            Args:
                size (int): size of a square
                position (int, int): the position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        get the attributes to be used in the class
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the value
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """
        retrieve the attributes of a class
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the value for position
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """
        Returns: area of current square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints to stdout the square with character #
        """
        if self.__size == 0:
            print()
        else:
            i = 0
            position1, position2 = self.__position
            for line in range(position2):
                print()
            while i < self.__size:

                j = 0
                while j < position1:
                    print(" ", end='')
                    j += 1

                num = 0
                while num < self.__size:
                    print("{}".format("#"), end='')
                    num += 1
                print()
                i += 1
