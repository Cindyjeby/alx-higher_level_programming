#!/usr/bin/python3

"""write a child class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """a subclass of class Base
    class Rectangle inherists fro Base
    private instance attribute, base with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize instance for class rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrive the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting and validating width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width= value

    @property
    def height(self):
        """retrive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting and validating height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height mustbe > 0")
        self.__height = value

    @property
    def x(self):
        """retrive x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter and validateing x"""
        if type(value) is not int:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

    @property
    def y(self):
        """retrive y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter and validating y"""
        if type(value) is not int:
            raise TypeError("y must be an interger")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """set area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print #  to the stdout"""
        for _ in range(self.__y):
            print()
            for k in range(self.__height):
                for j in range(self.__width + self.__x):
                    if j < self.__x:
                        print(" ", end="")
                        continue
                    print("#", end="")
                print()
    def __str__(self):
        """overriding __str__()"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        up = ["id", "width", "height", "x", "y"]
        if (args):
            for k in range(len(args)):
                setattr(self, up[k], args[k])

            else:
                for j in kwargs:
                    setattr(self, j, kwargs[j])

    def to_dictionary(self):
        """return dict rep of rectangle"""
        return {
            "x": self.x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
            }
