#!/usr/bin/python3
"""a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A class rectangle inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instantiation of the class rectangle
        with args:
            width (int): the width of rectangle.
            height (int): the height of rectangle.
            x (int): variable representing coordinates.
            y (int):variable representing coordinates.
            id (int): The identity, comes from the base class.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
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

        [print("") for y in range(self.y)]
        for j in range(self.height):
            print("{}".format(" ") * self.x + "{}".format("#") * self.width, end="")
            print()

    def __str__(self):
        """returns string representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    """def update(self, *args):
        'assigns an arg to each attribute'
        if args:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4] """

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.width = args[1]
            except IndexError:
                pass
            try:
                self.height = args[2]
            except IndexError:
                pass
            try:
                self.x = args[3]
            except IndexError:
                pass
            try:
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representation of the Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
                }
