#!/usr/in/python3
"""a class"""


class Student:
    """class has three attributes:
    first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """initializes student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dict representation of student"""
        return self.__dict__
