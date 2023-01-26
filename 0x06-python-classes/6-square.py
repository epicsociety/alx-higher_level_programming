#!/usr/bin/python3
""" A class """


class Square:
    """
    defines the class square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializes the class square
            Args:
                size: size of a square
                position: the position
        """
        self.__size = size
        self.__position = position

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
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            return self.__size == value

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
            return self.__position == value

    def area(self):
        """
        Returns: area of current square
        """
        return size.__self ** 2

    def my_print(self):
        """
        prints to stdout the square with character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" "*self.__position[0] + "#"*self.__size)
        #print()
        """integer = 0
            position1, position2 = self.__position
            for new_line in range(position2):
                print()
                while integer < self.__size:

                    j = 0
                    while j < position1:
                        print(" ", end='')  # replaces position with a space
                        j += 1

                        number = 0
                        while number < self.__size:
                            print("{}".format("#"), end='')
                            number += 1
                print()
                integer += 1"""
