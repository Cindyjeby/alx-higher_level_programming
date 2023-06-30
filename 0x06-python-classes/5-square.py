#!/usr/bin/python3

"""define a sqaure"""


class Square:
    """
    define a square class
    """
    def __init___(self, size=0):
        self.size = size

        @property
        def size(self):
            """gettter method for self.__size private variable"""
            return self.__size

        @size.setter
        def size(self, value):
            """setter method for self.__size private variable"""

            if type(value) != int:
                raise TypeError("size must be an intrger")
            if value < 0:
                raise ValueError("size must be >= 0")

                self.__size = value

                def area(self):
                    """return current sqaure area"""
                    return self.___size * self.___size

                def my_paint(self):
                    """print the square with the character #"""
                    if self.__size == 0:
                        print("")
                        for height in range(self.__size):
                            for width in range(self.__size):
                                print("#", end="")
                                print()
