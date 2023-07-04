#!/usr/bin/python3

"""create a class"""

class Rectangle:
    """reps a class"""

    number_of_instances = 0
    print_symbol = '#'

    def __int__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instance += 1

    @property
    def width(self):
        """getter for attribute"""
        return self.__width

    @width.setter
    def width(self,value):
        """setter for attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise Typeerror("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """setter for printer"""
        rectangle = ""
        if self.__width > 0 and self.__height > 0:
            for k in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """return a string"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__heigth)

    def __del__(self):
        """settes a del"""
        Rectangle.number_of_instance -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns area of the bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of the rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def sqaure(cls, size=0):
        """returns a new rectangle"""
        width = size
        height = size
        return cls(width, heigth)
