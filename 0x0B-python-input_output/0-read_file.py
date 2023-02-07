#!/usr/bin/python3
"""modules has one function that reads a file"""


def read_file(filename=""):
    """read_file reads a text file and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
