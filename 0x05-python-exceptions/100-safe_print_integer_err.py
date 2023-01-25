#!/usr/bin/python3


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        raise TypeError as ty
    except TypeError:
        return False
        print("Exception:", ty)
    else:
        return True

