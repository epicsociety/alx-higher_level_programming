#!/usr/bin/python3
"""Unittest for Base class

Unittest classes:
    testBase_instantiation
"""


class Test_Base_instantiation(unittest.TestCase):
    """class tests the constructor method"""

    def test_init_assigns_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_init_assigns_unique_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_init_assigns_given_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    if __name__ == "__main__":
        unittest.main()
