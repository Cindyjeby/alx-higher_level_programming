#!/usr/bin/python3

"""define a square class"""

class Square:
    """size is an int greater than 0"""
    self.__size = size

    @property
    def size(self):
        """getter method"""
        return self.__size
    @size.setter
    def size(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
            self._size = value

    def area(self):
        """return current area"""
        return self.__size *self.__size
