#!/usr/bin/python3

"""module is 3-is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    is a function that returns True if the object is an instance,
    or if the object is an instance of a class that inherited from,
    the specified classs
    False if otherwise
    """

    return isinstance(obj, a_class)
