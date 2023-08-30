#!/usr/bin/python3
"""define a class"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """initialize class"""
        self.size = size

    @property
    def size(self):
        """Get or set the size of class"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of class"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """define == operator to class"""
        return self.area() == other.area()

    def __ne__(self, other):
        """define the != operator to class"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < operator to class"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= operator to class"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > operator to a class"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= operator to a class"""
        return self.area() >= other.area()
