#!/usr/bin/python3
"""defines a BaseGeometry class"""

class BaseGeometry:
    """reps the BaseGeometry class"""

    def __init__(self):
        """instantiation for BaseGeometry class"""

        pass

    def area (self):
        """reps the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
