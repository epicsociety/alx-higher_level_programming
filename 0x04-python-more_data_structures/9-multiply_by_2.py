#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for key in a_dictionary:
        new[key] = a_dictionary[key] * 2
    return new
