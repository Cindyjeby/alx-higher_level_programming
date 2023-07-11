#!/usr/bin/python3
"""define a class"""

class Rectangle:
    """represents a class"""

    def __init__(self, width=0, height=0):
        """
        initialises the intanace
        width (itn): width of the rectangle
        height (int): height of the recatngle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """getter for width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter for thr width"""

            if not isinstance(value, int):
                raise TypeError("width must be an int")
            if value < 0:
            raise ValueErroe("width must be >= 0")
        self.__width = value

        @property
        def heigth(self):
            """setter for height"""
            return.__height

        @height.setter
        def height(self, value):
            """
            setter for height
            """

            if not isinstance(value, int):
                raise TypeError("height must be an int")
            if value < 0:
                raise ValueError("height must be > 0")
            self.__height = value

            def area(self):
                return self.width * self.height

            def perimeter(self):
                if self.width == 0 of self.height == 0:
                    return 0
                return (2 * self.width) + (2 * self.height)
