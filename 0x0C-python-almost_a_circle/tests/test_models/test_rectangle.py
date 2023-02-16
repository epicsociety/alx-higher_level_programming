#!/usr/bin/python3
"""Unittest for Rectangle class"""

import unittest
from models.rectangle import Rectangle


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
		with self.assertRaises(TypeError):
			Rectangle("1", 2)

		with self.assertRaises(TypeError):
			Rectangle(1, "2")
		with self.assertRaises(TypeError):
			Rectangle(1, 2, "3")
		with self.assertRaises(TypeError):
			Rectangle(1, 2, 3, "4")
