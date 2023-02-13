#!/usr/bin/python3
"""a base class"""
import json
import csv
import turtle
import tkinter


class Base:
    """the definition of the base class"""
    __nb_objects = 0  #private class attribute

    def __init__(self, id=None):
        """instantiation of the base class"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries
        Arg:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """returns JSON string representation of list_objs to a file
        Args:
            list_objs (list): a list of instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_string = Base.to_json_string(list_dicts)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """return a list of the JSON string representation json_string
        Args:
            json_string (str): string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
                new.update(**dictionary)
                return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings
        Reads from `<cls.__name__>.json`
        Returns an empty list if the file does not exist
                or a list of instantiated classes if it does
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file
        Args:
            list_objs (list): A list of inherited Base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file
        Reads from `<cls.__name__>.csv`
        Returns an empty string if file does not exist
                or a list of instantiated classes
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([key, int(value)] for key, value in d.items()) 
                                for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []


    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module
         Args:
             list_rectangles (list): A list of Rectangle objects to draw
             list_squares (list): A list of Square objects to draw
        """
        rootwindow = tkinter.Tk()
        rootwindow.mainloop()

        turt = turtle.Turtle()
        turt.screen.bgcolor("#b5e3d8")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b7312c")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
