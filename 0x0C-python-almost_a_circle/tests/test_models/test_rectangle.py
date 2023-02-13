#!/usr/bin/python3
"""Unittest for Rectangle class"""


import unittest
from models import base
from models.base import Base
from models import rectangle
from models.rectangle import Rectangle
import sys
Base = Base
Rectangle = Rectangle
to_json_string = Base.to_json_string
from_json_string = Base.from_json_string
save_to_file = Base.save_to_file
load_from_file = Base.load_from_file
create = Base.create
update = Rectangle.update
to_dic = Rectangle.to_dictionary
area = Rectangle.area
display = Rectangle.display


class TestsRectangle(unittest.TestCase):
    def test_docs(self):
        """Tests"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_to(self):
        """Tests"""
        self.assertTrue(len(to_json_string.__doc__) > 0)

    def test_from(self):
        """Tests"""
        self.assertTrue(len(from_json_string.__doc__) > 0)

    def test_save(self):
        """Tests"""
        self.assertTrue(len(save_to_file.__doc__) > 0)

    def test_load(self):
        """Tests"""
        self.assertTrue(len(load_from_file.__doc__) > 0)

    def test_create(self):
        """Tests"""
        self.assertTrue(len(create.__doc__) > 0)

    def test_docs1(self):
        """Tests"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_to1(self):
        """Tests"""
        self.assertTrue(len(to_json_string.__doc__) > 0)

    def test_from1(self):
        """Tests"""
        self.assertTrue(len(from_json_string.__doc__) > 0)

    def test_save1(self):
        """Tests"""
        self.assertTrue(len(save_to_file.__doc__) > 0)

    def test_load1(self):
        """Tests"""
        self.assertTrue(len(load_from_file.__doc__) > 0)

    def test_create1(self):
        """Tests"""
        self.assertTrue(len(create.__doc__) > 0)

    def test_docs2(self):
        """Tests"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_to2(self):
        """Tests"""
        self.assertTrue(len(to_json_string.__doc__) > 0)

    def test_from2(self):
        """Tests"""
        self.assertTrue(len(from_json_string.__doc__) > 0)

    def test_save2(self):
        """Tests"""
        self.assertTrue(len(save_to_file.__doc__) > 0)

    def test_load2(self):
        """Tests"""
        self.assertTrue(len(load_from_file.__doc__) > 0)

    def test_create2(self):
        """Tests"""
        self.assertTrue(len(create.__doc__) > 0)

    def test_docs3(self):
        """Tests"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_to3(self):
        """Tests"""
        self.assertTrue(len(to_json_string.__doc__) > 0)

    def test_from3(self):
        """Tests"""
        self.assertTrue(len(from_json_string.__doc__) > 0)

    def test_save3(self):
        """Tests"""
        self.assertTrue(len(save_to_file.__doc__) > 0)

    def test_load3(self):
        """Tests"""
        self.assertTrue(len(load_from_file.__doc__) > 0)

    def test_create3(self):
        """Tests"""
        self.assertTrue(len(create.__doc__) > 0)

if __name__ == '__main__':
    unittest.main()
