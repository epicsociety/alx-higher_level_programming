#!/usr/bin/python3
"""a class Square"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """class Square that inherits all attributes from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiate Square with attributes from Rectangle
        Args:
            size (int): The size of the new Square.
            x (int): a variable, coordinate of the new Square.
            y (int): a variable, coordinate of the new Square.
            id (int): The identity of the new Square.
        all of the args are contributed by Rectangle class
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """getter for size"""
        return self.width or self.height

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes
        *args:
            - 1st argument should be the id attribute
            - 2nd argument should be the size attribute
            - 3rd argument should be the x attribute
            - 4th argument should be the y attribute
        """
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
                n += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dictionary representation of the Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y,
                }
    def __str__(self):
        """returns string representation of Square"""
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width or self.height))
