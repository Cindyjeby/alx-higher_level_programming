#!/usr/bin/python3

"""define a Square"""


class Square:
    """defines a class Square"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.___size = size

    def area(self):
        """returns current square area"""
        return self.__size * self.__size
