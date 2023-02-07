#!/usr/bin/python3
"""Module that prints sorted list"""


class MyList(list):
    """subclass that inherits from list"""
    def print_sorted(self):
        """prints ascending sorted list"""
        print(sorted(self))
