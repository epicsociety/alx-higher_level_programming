#!/usr/bin/python3
"""module contains only one method that appends a string"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
