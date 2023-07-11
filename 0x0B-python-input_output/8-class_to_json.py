#!/usr/bin/python3

"""defines a class-to-JSON function"""

def class_to_json(obj):
    """retuns the dictionary rep of a simple data structure"""
    return obj.__dict__
