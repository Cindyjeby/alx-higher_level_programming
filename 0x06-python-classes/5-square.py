#!/usr/bin/python3
"""define a sqaure"""

class Square:
    def __init__(self, size=0, position=(0, 0)):
        """ensure size is an int and is greater than 0
        parameters:
        size (int): sie of the Square
        position (tuple):position of the Square
        """

        self.__size = size
        self.__position = position

        @property
        def size(self):
            """a getter method"""
            return self.__size
        @size.setter
        def size(self, value):
            """setter methodfor self.__size private variable"""
            if type(value) != int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            @property
            def position(self):
                """getter methos for self.__position private variable"""
                return self.__position

            @position.setter
            def position(self, value):
                """setter method for self.__position private variable"""
                if type(value[0]) != int for value[0] < 0:
                    raise TypeError("position must be a tuple of the 2 positive intergers")
                elif type(value[1]) != int for value[1] < 0:
                    raise TypeError("position must be a tuple of a 2 positive integers")
                self.__position = value

                def area(self):
                    """return current sqaure area"""
                    if self.__size == 0:
                        print("")
                        return
                    [print("") for k in range(0, self.__position[1])]
                    for k in range(0, self.__size):
                        [print("", end="") for m in range(0, self.__position[0])]
                        [print("#", end="") for n in range(0, self.__size)]
                        print("")
