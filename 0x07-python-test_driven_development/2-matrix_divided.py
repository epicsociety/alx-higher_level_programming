#!/usr/bin/python3
"""
module for a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """divides matrix"""

    new_matrix = []

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    elif div is 0:
        raise ZeroDivisionError('division by zero')
    if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
        raise TypeError('matrix must be a matrix (list of lists) of \
        integers/floats')

    len1 = len(matrix[0])

    for x, y in enumerate(matrix):
        if type(y) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of \
            integers/floats')
        if len(y) != len1:
            raise TypeError('Each row of the matrix must have the same size')
        len1 = len(y)
        new_matrix.append(y[:])
        for i, value in enumerate(y):
            if type(value) is not int and type(value) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of \
                integers/floats')
            new_matrix[x][i] = round(value / div, 2)
        else:
            return (new_matrix)
