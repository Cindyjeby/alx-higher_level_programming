#!/usr/bin/python3
"""defines a function inherits_from"""

def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance
    of a class that inherited (directly of indirectly) from
    specified class
    False if otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
