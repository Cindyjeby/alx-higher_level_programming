#!/usr/bin/python3
"""defines a class"""

class Rectangle:
    """represents the class"""

    def __init__(self, width=0, height=0):
        """
        to initialize when an instance is cearted

        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """getter for width"""

            return self.__width

        @width.setter
        def width(self, value):
            """setter for width private instance variable

            value (int): size of the width

            raises:
            TypeError: when value is not int
            ValueError: is less than 0
            """

            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """setter for heigth"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter for height

            value (int): size of the height
            """

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
