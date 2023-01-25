#!/usr/bin/python3
'''A Defining the class Square'''


class Square:
    '''A class square
    Attruiutes: __size (int): size of side of a square'''

    def __init__(self, size=0):
        '''Initializes a square
        Args:
            size:size of one side of a square
        '''

        try:
            type(size) is int
        except TypeError:
            print("size must be an interger")
        try:
            size > 0
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size
