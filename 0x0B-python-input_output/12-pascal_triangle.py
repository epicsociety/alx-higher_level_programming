#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    for i in range(n):
        if i == 0:
            pascal_list = [[1]]
        else:
            row = [1]
            for j in range(1, i):
                row.append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
            row.append(1)
            pascal_list.append(row)
    return pascal_list
