#!/usr/bin/python3
"""defines a class"""


class Rectangle:

    """
    a class attribute used to keep count of numbe of instances
    """
    number_of_instances = 0

    """A class/public attribute used to print Rectange"""
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        instantiation with height and weight
        height: height of rectangle
        width: width of rectagle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width a private atrribute"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height, a private attribute"""

        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = int((2 * self.__height) + (2 * self.__width))

        return perimeter

    def __str__(self):
        """prints a string representation of the rectangle"""
        rectangle = []
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle.append(str(self.print_symbol))
                if i < self.__height - 1:
                    rectangle.append("\n")
            rectangle = "".join(rectangle)
            return rectangle

    def __repr__(self):
        """
        returns a string representation of the rectangle
        to be used with eval() in recreating a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when rectangle is deleted"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        """ a rectangle instance where width=height=size"""
        return cls(width=size, height=size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area"""
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
