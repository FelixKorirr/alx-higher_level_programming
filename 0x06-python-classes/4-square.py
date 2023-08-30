#!/usr/bin/python3
"""define class"""


class Square:
    """represent class"""

    def __init__(self, size=0):
        """Initialize class"""

        self.size = size

    @property
    def size(self):
        """Get/set the size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of square."""
        return (self.__size * self.__size)
