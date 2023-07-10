#!/usr/bin/python3

"""defines a rectangle class that inherits from BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A subclass of baseGeometry"""

    def __init__(self, width, height):
        """initialize private attribute"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
