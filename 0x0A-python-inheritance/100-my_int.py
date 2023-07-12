#!/usr/bin/python3

"""write a class myint that inherits from int"""


class MyInt(int):
    """a subclass of class int"""
    def __eq__(self, other):
        """sets the behaviour of =="""
        return int(self) != other

    def __ne__(self, other):
        """sets the != behaviour"""
        return int(self) == other
