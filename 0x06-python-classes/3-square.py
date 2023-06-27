#!/usr/bin/bash
"""define a Square"""

class Square:
    """defines a class Square"""

    def __init__(self, size=0):
        """makes sure that size is an int and is greater than 0"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """returns current square area"""
        return self.__size * self.__size
