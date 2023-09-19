#!/usr/bin/python3
"""Defines a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square subclass."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square class."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square class."""
        if args and len(args) != 0:
            a = 0
            for a in args:
                if a == 0:
                    if a is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = a
                elif a == 1:
                    self.size = a
                elif a == 2:
                    self.x = a
                elif a == 3:
                    self.y = a
                a += 1

        elif kwargs and len(kwargs) != 0:
            for p, q in kwargs.items():
                if p == "id":
                    if q is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = q
                elif p == "size":
                    self.size = q
                elif p == "x":
                    self.x = q
                elif p == "y":
                    self.y = q

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return string representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
