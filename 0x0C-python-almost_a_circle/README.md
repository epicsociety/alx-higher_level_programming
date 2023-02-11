
This directory entails a dive deep into unittest in python

-------------------
The Basics of unittest
---------------------

-> The unittest module provides a rich set of tools for constructing and running tests.
-> A testcase is created by subclassing unittest.TestCase

-> The crux of each test is a call to assertEqual() to check for an expected result; assertTrue() or assertFalse() to verify a condition; or assertRaises()

-> The setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method. 

-> Test modules can be specified by file path as well:

python -m unittest tests/test_something.py

-> You can run tests with more detail (higher verbosity) by passing in the -v flag:

python -m unittest -v test_module

