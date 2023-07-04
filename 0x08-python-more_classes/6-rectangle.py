#!/usr/bin/python3
"""defines a rectangle"""

class Rectangle:
    """reps a class rectangle"""
    
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialisd when an instance is created"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retruve attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
                raise TypeError("width must be an integer")
        if ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """to retrive attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """find area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """finds perimeter of the rectangle"""
        if self.__width == 0 of self.__height == 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        """sets the print"""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for size in range(self.__height):
                rectangle += '#' * self.__width + '\n'

        return rectangle[:-1}

    def __repr__(self):
        """returns a string"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """stes the del"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
