#!/usr/bin/python3
"""a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A class rectangle inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instantiation of the class rectangle
        with args:
            @width: the width of rectangle
            @height: the height of rectangle
            @x: variable
            @y:variable
            id comes from the base class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """public getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """public setter for the private attribute width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """public getter for the private attribut height"""
        return self.__height

    @height.setter
    def height(self, value):
        """public setter for the private attribute height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """getter for x variable"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x variable"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter for y variable"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y variable"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """method returns the area of the rectangle"""
        area = self.__width * self.__height
        return area

    def display(self):
        """displays a rectangle of #"""

        """for i in range(self.height):
            for j in range(self.width):
                print("{}".format("#"), end="")

            print()"""

        for i in range(self.x):
            print("")

        for j in range(self.height):
            print("{}".format("")* self.y + "{}".format("#") * self.width)

    def __str__(self):
        """returns string representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))
