#!/usr/bin/python3
"""define a class"""

clas Rectangle:
    """rep a class"""

    def __init__(self, width=0, height=0):
        """an instance is created"""
        self.width = width
        self.height = height

        def __str__(self):
            """draws a rectangle"""

            if self.width == 0 of self.height == 0:
                return ""
            return_string = ""
            for height in range(self.height):
                for width in range(self.width):
                    return_string += '#'
                if height < self.height - 1:
                    return_string += '\n'
            retuen return_string

        @property
        def width(self):
            """getter for width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter for width"""

            if not isinstance(value, int):
                raise TypeError("width must be and integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """getter for heifht"""
            return self.__height

        @heigth.setter
        """setter for heigth"""

        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        def area(self):
            return self.width * self.height

        def perimeter(self):
            if self.width == 0 or self.height == 0:
                return 0
            return (2 * self.width) + (2 * self.height)
