#!/usr/bin/python3
"""Unittest for Square class"""

import unittest
import json
from models.square import Square


# Test for square starts here
class TestSquareInit(unittest.TestCase):
    """Test for instantiation of the square"""

    def test_square_init_size(self):  # Provided one agr
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_init_size_and_x(self):  # Provided two args
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_square_init_size_x_and_y(self):  # Provided three args
        s = Square(1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_init_string_size(self):  # Provided a string arg
        with self.assertRaises(TypeError):
            s = Square("1")

    def test_square_init_size_and_string_x(self):
        with self.assertRaises(TypeError):
            s = Square(1, "2")

    def test_square_init_size_x_and_string_y(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")

    def test_square_init_size_x_y_and_id(self):  # Provided four args
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_square_init_negative_size(self):  # Provided one negative value
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_square_init_size_and_negative_x(self):
        with self.assertRaises(ValueError):
            s = Square(1, -2)

    def test_square_init_size_x_and_negative_y(self):
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)

    def test_square_init_zero_size(self):  # Provided a zero as an arg
        with self.assertRaises(ValueError):
            s = Square(0)


class TestSquareMethods(unittest.TestCase):
    """ Tests for __str__ and to_dictionary methods"""

    def test_str_method(self):  # Does __str__ return string representation
        s = Square(2, 2, 2, 1)
        self.assertEqual(str(s), '[Square] (1) 2/2 - 2')

    # Successful input of data to a dictionary
    def test_to_dictionary_method(self):
        s = Square(2, 2, 2, 1)
        s_dict = s.to_dictionary()
        expected_dict = {'id': 1, 'size': 2, 'x': 2, 'y': 2}
        self.assertDictEqual(s_dict, expected_dict)


class TestSquareUpdate(unittest.TestCase):
    """Tests whether the update methods work as expected"""

    def test_update(self):
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        s1 = Square(5)
        s1.update(id=10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")

        s1.update(size=1, id=2)
        self.assertEqual(s1.__str__(), "[Square] (2) 0/0 - 1")

        s1.update(x=3, size=1, id=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 1")

        s1.update(y=4, x=3, size=1, id=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 1")

    def test_update_args_kwargs(self):
        s1 = Square(5)
        s1.update(10, id=20)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")

        s1.update(1, 2, id=2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3, id=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4, id=5)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_update_type_error(self):
        s1 = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(10, "2")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(10, 2, "3")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(10, -2)


class TestSquareCreate(unittest.TestCase):
    """Tests that create method works properly as expected"""

    def test_create_with_id(self):
        s = Square.create(**{'id': 89})
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)

    def test_create_with_id_and_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_create_with_id_size_and_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_create_with_id_size_x_and_y(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)


class TestSquareFiles(unittest.TestCase):
    """Tests if save and load file works"""


@classmethod
def setUpClass(cls):
    cls.s1 = Square(5)
    cls.s2 = Square(2, 2)
    cls.s3 = Square(3, 1, 3)
    cls.s4 = Square(4, 0, 0, 10)


def tearDown(self):
    try:
        os.remove("Square.json")
    except Error:
        pass


def test_save_to_file_None(self):
    Square.save_to_file(None)
    with open("Square.json", "r") as file:
        self.assertEqual(file.read(), "[]")


def test_save_to_file_empty_list(self):
    Square.save_to_file([])
    with open("Square.json", "r") as file:
        self.assertEqual(file.read(), "[]")


def test_save_to_file(self):
    Square.save_to_file([self.s1, self.s2])
    with open("Square.json", "r") as file:
        self.assertEqual(len(file.read()), 78)


def test_load_from_file_no_file(self):
    self.assertEqual(Square.load_from_file(), [])


def test_load_from_file(self):
    Square.save_to_file([self.s1, self.s2])
    list_squares = Square.load_from_file()
    self.assertEqual(len(list_squares), 2)
    self.assertIsInstance(list_squares[0], Square)
    self.assertIsInstance(list_squares[1], Square)
    self.assertEqual(list_squares[0].__str__(), "[Square] (1) 0/0 - 5")
    self.assertEqual(list_squares[1].__str__(), "[Square] (2) 2/0 - 2")


if __name__ == '__main__':
    unittest.main()
