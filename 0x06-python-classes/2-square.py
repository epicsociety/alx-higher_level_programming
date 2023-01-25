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

        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an interger")
