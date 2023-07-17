#!/usr/bin/python3

"""write the first class base"""

import json
import csv
import turtle


class Base:
    """the base class"""
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            base.__nb_object += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        obj_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_dicts)
        with open(filename, mode='w', encode='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """return the list of json string"""
        if json_string is None or json_string == []:
            return []
        else:
            returnjson.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with set attributes"""
        if cls.__name__ == "Rectangle":
            deummy = cls(1, 1)
        else:
            dummy = cls(1)
            dummy.update(**dictionary)
            return (dummy)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                list = cls.from_json_string(file.read())
                return [cls.create(**dic) for dic in list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves the list"""
        filename = cls.__nmae__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                #write directories to the CSV file
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        """reads data from CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ ++ "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                    list = csv.DictReader(file, fieldnames=fieldnames)

                    list = [dict([k, int(v)] for k, v in d.items())
                            for d in list]
                    return [cls.create(**d) for d in list]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_square):
        """draws a rectangle and sqaure using the turtle module"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for k in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for k in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
