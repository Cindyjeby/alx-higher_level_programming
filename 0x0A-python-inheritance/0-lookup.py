#!/usr/bin/python3
"""defines an attribute and object lookup function"""


def lookup(obj):
    """returns a list of all the available attributes and methods"""

    return dir(obj)
