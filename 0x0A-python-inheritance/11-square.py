#!/usr/bin/python3
"""defines a class Square"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """reps a square class"""

    def __init__(self, size):
        """initialize Square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """string method for sqaure class"""

        return "[Square] {}/{}".format(self.__size, self.__size)
