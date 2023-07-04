#!/usr/bin/python3
"""defines a class"""

class Rectangle:
    """represents a class """

    def __init__(self, width=0, height=0):
        """when a instance is created
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__9self):
        """draws a rectangle using the character #"""

        if self.width == 0 or self.height == 0:
            return ""
        return_string = ""
        for height in range(self.height):
            for width in range(self.width):
                return_string += '#'
            if heigth < self.height - 1:
                return_string += '\n'
        return return_string

    def __repr__(self):
        """return a string rep of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width

        parameters:
        value (int): size of the width

        raises:
        Typeerror: if the value is not an interger
        ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for width private instance variable

        Parameters:
        value (int): size ofr the height

        Raises:
        TypeError: if the value is not an integer
        ValueError: if the value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)
