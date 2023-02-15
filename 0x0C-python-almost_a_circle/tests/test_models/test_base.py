#!/usr/bin/python3
"""Unittest for Base class

Unittest classes:
    testBase_instantiation
"""
import unittest
from models.base import Base


class Test_Base_instantiation(unittest.TestCase):
    """class tests the constructor method"""

    def test_init_assigns_id(self):
        b1 = Base()
        self.assertEqual(b1.id, b1.id)

    def test_init_assigns_unique_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases_id_assigns(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_init_assigns_given_id(self):
        b1 = Base(9)
        self.assertEqual(b1.id, 9)

    def test_after_unique_id(self):
        b1 = Base()
        b2 = Base(9)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)


class Test_Base_to_json_string(unittest.TestCase):
    """testing the Base.to_json_string instances"""

    def setUp(self):
        Base._Base_nb_objects = 0

    def test_to_json_string(self):
        # Test with an empty string
        self.assertEqual(Base.to_json_string([]), "[]")

        #test with None
        self.assertEqual(Base.to_json_string(None), "[]")

        #test with a list of dictionaries
        list_dictionaries = [{"id": 1}, {"id": 2}]
        expected = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(Base.to_json_string(list_dictionaries), expected)

    if __name__ == "__main__":
        unittest.main()
