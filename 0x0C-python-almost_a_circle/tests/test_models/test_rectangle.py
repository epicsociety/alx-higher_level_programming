#!/usr/bin/python3
"""Unittest for Rectangle class"""

import io
from models.rectangle import Rectangle
from unittest.mock import patch
import unittest
import sys


class TestRectangle(unittest.TestCase):
    # testing with valid int arguments
    def test_init_with_valid_arguments(self):
        """testing with any two args"""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_init_with_three_arguments(self):
        """testing with any three int args"""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_init_with_four_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertIsNotNone(r.id)

    # Testing with invalid arguments i.e nonnumric values
    def test_rectangle_with_non_numeric_arguments(self):
        """runs several tests that pass a string as arg for dimensions"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    # Testing for five args
    def test_rectangle_with_five_args(self):
        """checks instantiation with five arguments"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    # Testing for zero and negative args
    def test_rectange_with_zero_or_negative_args(self):
        """tests rectangle instantiation with zero or negative values"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    # Testing for area of the rectange
    def test_rectangle_area(self):
        """tests whether area () works"""
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    # Testing for __str__ of the rectangle
    def test_rectangle_str(self):
        """tests __str__work"""
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (6) 4/5 - 2/3")


# Testing for display of rectangle
class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.
        Args:
            rect (Rectangle) - The Rectangle to print to stdout
        method (str) - The method to run on rect.
        Returns:
        The text printed to stdout by calling method on sq.
        """

        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_rectangle_display_without_xy(self):
        """testing display without x and y args"""
        r = Rectangle(2, 3)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_rectangle_display_without_y(self):
        """testing display without y arg"""
        r = Rectangle(2, 3, 4)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("    ##\n    ##\n    ##\n", capture.getvalue())

    def test_rectangle_display_with_xy(self):
        """testing where both x and y are present"""
        r = Rectangle(2, 3, 1, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("\n ##\n ##\n ##\n", capture.getvalue())

    # Testing for dictionary
    def test_rectangle_to_dictionary(self):
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.to_dictionary(), {'x': 4, 'y': 5, "id": 6, "width": 2, "height": 3})


# Testing the update method for both *args and **kwargs
class TestRectangleUpdate(unittest.TestCase):
    """class tests for the update methods of class Rectangle"""

    def test_rectangle_update(self):
        """tests a normal Rectangle"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_rectangle_update_id(self):
        """test for updating with the id"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_rectangle_update_id_width(self):
        """Testing update id and width"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(89, 1)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_rectangle_update_id_width_height(self):
        """Testing update id width and height"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(89, 1, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_update_id_width_height_x(self):
        """Testing update id, width, height and x"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_rectangle_update_id_width_height_x_y(self):
        """Testing everything updated"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    # Test for **kwargs start here
    def test_update_kwargs(self):
        """this tests whether update *args and **kwargs works"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(**{'id': 2})
        self.assertEqual(r.__str__(), "[Rectangle] (2) 0/0 - 1/1")
        r.update(**{'id': 3, 'width': 4})
        self.assertEqual(r.__str__(), "[Rectangle] (3) 0/0 - 4/1")
        r.update(**{'id': 5, 'width': 6, 'height': 7})
        self.assertEqual(r.__str__(), "[Rectangle] (5) 0/0 - 6/7")
        r.update(**{'id': 8, 'width': 9, 'height': 10, 'x': 11})
        self.assertEqual(r.__str__(), "[Rectangle] (8) 11/0 - 9/10")
        r.update(**{'id': 12, 'width': 13, 'height': 14, 'x': 15, 'y': 16})
        self.assertEqual(r.__str__(), "[Rectangle] (12) 15/16 - 13/14")

    # Test for create start here
    def test_create_kwargs(self):
        """This one tests whether create works well with one or more args"""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.__str__(), "[Rectangle] (89) 0/0 - 1/1")
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.__str__(), "[Rectangle] (89) 0/0 - 1/1")
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.__str__(), "[Rectangle] (89) 0/0 - 1/2")
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.__str__(), "[Rectangle] (89) 3/0 - 1/2")
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.__str__(), "[Rectangle] (89) 3/4 - 1/2")


# Test for save_to_file starts here

@classmethod
def setUpClass(cls):
    """Set up the testing environment."""
    cls.r = Rectangle(1, 1, 0, 0, 1)

@classmethod
def tearDownClass(cls):
    """Remove the test file."""

    try:
        os.remove("Rectangle.json")
    except FileNotFoundError:
        pass


def test_save_to_file_None(self):
    """Test if save_to_file() saves an empty list if the input is None."""
    Rectangle.save_to_file(None)
    with open("Rectangle.json", "r") as f:
        self.assertEqual("[]", f.read())


def test_save_to_file_empty_list(self):
    """Test if save_to_file() saves an empty list if the input is an empty list."""
    Rectangle.save_to_file([])
    with open("Rectangle.json", "r") as f:
        self.assertEqual("[]", f.read())


def test_save_to_file_one_rectangle(self):
    """Test if save_to_file() saves a list with one Rectangle."""
    Rectangle.save_to_file([self.r])
    with open("Rectangle.json", "r") as f:
        self.assertEqual(f.read(), f"[{self.r.to_dictionary()}]")


def test_load_from_file(self):
    """Test if load_from_file() correctly loads a list of Rectangles from a file."""
    # Create a list of Rectangles to save to file
    rects = [Rectangle(1, 2, 3, 4), Rectangle(5, 6, 7, 8)]
    Rectangle.save_to_file(rects)

    # Load the Rectangles from the file
    loaded_rects = Rectangle.load_from_file()

    # Check that the loaded list has the correct number of Rectangles
    self.assertEqual(len(loaded_rects), len(rects))

    # Check that each Rectangle in the loaded list has the correct attributes
    for i in range(len(rects)):
        self.assertEqual(loaded_rects[i].id, rects[i].id)
        self.assertEqual(loaded_rects[i].width, rects[i].width)
        self.assertEqual(loaded_rects[i].height, rects[i].height)
        self.assertEqual(loaded_rects[i].x, rects[i].x)
        self.assertEqual(loaded_rects[i].y, rects[i].y)


if __name__ == '__main__':
    unittest.main()
