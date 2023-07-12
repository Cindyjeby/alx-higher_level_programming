#!/usr/bin/python3

"""defines a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """reps a square"""

    def __init__(self, size):
        """initalize a square class"""
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """returns area"""
        return self.__size ** 2
