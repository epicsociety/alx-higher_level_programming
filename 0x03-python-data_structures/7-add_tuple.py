#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_tuple = [0, 0]
    new_tuple = (tuple_a, tuple_b)
    for x in range(2):
        if len(new_tuple[0]) > x:
            my_tuple[x] += new_tuple[0][x]
        if len(new_tuple[1]) > x:
            my_tuple[x] += new_tuple[1][x]
    return (my_tuple[0], my_tuple[1])
