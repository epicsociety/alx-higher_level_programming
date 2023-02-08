#!/usr/bin/python3
"""a class"""


class Student:
    """class has three attributes:
    first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """initializes student class
        args:
        first_name (str): name
        last_name (str): name
        age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        gets dict representation of student instance
        if attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        args:
        attrs (list): probably present
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

        def reload_from_json(self, json):
            """replaces all attrs if the student instance"""
            for attr, value in json.items():
                setattr(self, attr, value)
