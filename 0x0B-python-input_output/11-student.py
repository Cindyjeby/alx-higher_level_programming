#!/usr/bin/python3

"""define a Student class"""

class Student:
    """define a Student"""

    def __init__(self, first_name, last_name, age):
        """initialize for student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrive a dictionary"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
