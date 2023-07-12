#!/usr/bin/python3

"""defines a student class"""


class Student:
    """defines Student"""

    def __init__(self, first_name, last_name, age):
        """initalize method for student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrive a dictionary"""

        return self.__dict__
