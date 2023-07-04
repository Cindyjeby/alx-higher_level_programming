#!/usr/bin/python3

"""create a class"""

class Rectangle:
    """reps a class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init(self, width=0, height=0):
        self.height = height
        self.widht = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrive attribute"""
        return self.__width

    @width.setter
    """setter for attribute"""
    if type(value) is not int:
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueErro("width must be >= 0")

    self.__width = value

    @property
    def height(self):
        """retrive attribute"""
        return self.__heigth

    @height.setter
    def height(self, value):
        """setter for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise valueError("height must be >= 0")

        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """sets the print"""
        rectangle = ""
        if self.__width > 0 and self.__height > 0:
            for k in range(self.__height)):
                rectangle += str (self.print_symbol) * self.__width + '\n'
        return rectangle[:-1]

    def __repr__(self):
        """return a string"""
        return "Rectangle ({:d},{:d})".format(self.__width, self.__height)

    def __del__(self):
        """sets the del"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
