#!/usr/bin/python3
"""module contains only one method that writes a string to text file"""


def write_file(filename="", text=""):
    """
    writes a string to text file and returns the numbe of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
