#!/usr/bin/python3

"""Define a Square"""

class Square:
    """
    square class with a private attribute size
    and checks data type
    """
    def __int__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
