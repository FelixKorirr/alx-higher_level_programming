#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, p=0, y=0, id=None):
        """Initialize a new class Square"""
        super().__init__(size, size, p, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square class"""
        if args and len(args) != 0:
            a = 0
            for p in args:
                if a == 0:
                    if p is None:
                        self.__init__(self.size, self.p, self.y)
                    else:
                        self.id = p
                elif a == 1:
                    self.size = p
                elif a == 2:
                    self.p = p
                elif a == 3:
                    self.y = p
                a += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.p, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "p":
                    self.p = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
        """Returns dictionary representation of Square class"""
        return {
            "id": self.id,
            "size": self.width,
            "p": self.p,
            "y": self.y
        }

    def __str__(self):
        """Returns string representation of Square class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.p, self.y,
                                                 self.width)
