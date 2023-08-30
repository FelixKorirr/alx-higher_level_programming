#!/usr/bin/python3
"""define class"""


class Square:
    """represent class"""

    def __init__(self, size):
        """initialize class"""
        self.size = size

    @property
    def size(self):
        """Get/set size of the class"""
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

    def my_print(self):
        """print square with # character."""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
