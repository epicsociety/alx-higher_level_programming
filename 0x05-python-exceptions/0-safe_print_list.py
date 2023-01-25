#!/usr/bin/python2


def safe_print_list(my_list=[], x=0):
    """ Prints x elements of a list
    my_list: list of elements to be printed
    x: number of elements to be printed
    """

    elements_printed = 0
    for i in range(x):
        try:
            print(my_list[i], end=" ")
            elements_printed += 1
        except IndexError:
            pass
    print()
    return elements_printed
