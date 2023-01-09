#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in range(len(matrix)):
            for element in range(len(matrix[row])):
                if element != len(matrix[row]) - 1:
                    punc = " "
                else:
                    punc = ""
                print("{:d}".format(matrix[row][element]), end=punc)
            print()
