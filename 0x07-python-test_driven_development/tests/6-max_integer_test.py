#!/usr/bin/python3
"""Unittest for max_integer([.])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_import(self):
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def test_noargs(self):
        self.assertIsNone(max_integer())

    def test_onearg(self):
        self.assertEqual(max_integer([69]), 69)

    def test_str(self):
        self.assertEqual(max_integer("1424351423241"), "5")
        self.assertEqual(max_integer("1, 3, 6"), "6")

    def test_neg_int(self):
        self.assertEqual(max_integer([-23, -43, -69, -2]), -2)
        self.assertEqual(max_integer([23, 43, -69, 2]), 43)

    def test_float(self):
        self.assertEqual(max_integer([-23.2, -43.9, -69.6, -2.9]), -2.9)
        self.assertEqual(max_integer([23.2, 43.9, -69.6, 2.9]), 43.9)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
