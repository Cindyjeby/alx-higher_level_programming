#!/usr/bin/python3

"""the module is 2-is_same_class"""


def is_same_class(obj, a_class):
    """
    checks if the object is the same as the instance of the class
    returns True if the object is exactly an instance of the class
    returns False otherwise
    """

    return type(obj) is a_class
