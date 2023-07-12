#!/usr/bin/python3
"""the module is 9-rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass of baseGeometry class"""

    def __init__(self, width, height):
        """initializes private attribute"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """returns readable string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """reps the area"""
        return self.__height * self.__width
