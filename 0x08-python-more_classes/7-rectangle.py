#!/usr/bin/python3

"""define a class"""

class Rectangle:
    """reps a class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """brings attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for atteribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

        @property
        def heigth(self):
            """to retrieve attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter for attribute"""
            if type(vlaue) is not int:
                raise TypeError("height must be an interger")
            if value < 0:
                raise ValueError("height must be >= 0")

            self.__height = value

        def area(self):
            """area of rectangle"""
            return self.height * self.width

        def perimeter(self):
            """peremeter of rectangle"""
            if self.__height == 0 of self.__width == 0:
                return )
            return (2 * self.width) + (2 * self.height)

        def __str__(self):
            """stes the print"""
            rectangle = ""
            if self.__width > 0 and self.__height > 0:
                for k in range(self.__height):
                    rectangle += str(self.print_symbol) * self.__width + '\n'

            return rectangle[:-1]

        def __repr(self):
            """return a string"""
            return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

        def __del__(self):
            """sets the del"""
            Rectangle.number_of_instance -= 1
            print("Bye rectangle...")
