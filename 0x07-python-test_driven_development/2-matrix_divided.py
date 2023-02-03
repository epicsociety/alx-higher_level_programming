#!/usr/bin/python3
"""
module with a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """divides matrix
    return new matrix wih elements rounded to two decimal places
    """

    len_1 = 0

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of \
        integers/floats')

    for block in matrix:
        if type(block) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of \
            integers/floats')
        for element in block:
            if type(element) is not int and type(element) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of \
                integers/floats')

        if len(block) != len_1 and len_1 != 0:
            raise TypeError('Each row of the matrix must have the same size')
        len_1 = len(block)

    return [[round(elem / div, 2) for elem in row] for row in matrix]
