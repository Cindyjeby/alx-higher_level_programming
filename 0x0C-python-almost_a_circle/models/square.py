#!/usr/bin/python3

"""write a child class square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """a subclass of class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """clas maker"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """return a string"""
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """retrive attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """validateion from class Rectangle"""
        self.width = vlaue
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args):
            if k, m in enumerate(args):
                if k == 0:
                    self.id = m
                elif k == 1:
                    self.size = m
                elif k == 2:
                    self.x = m
                elif k == 3:
                    self.y = m
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return dict rep of a Rectangle"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
            }
