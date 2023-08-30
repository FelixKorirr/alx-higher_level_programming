#!/usr/bin/python3
"""define class"""


class Square:
    """represent class"""

    def __init__(self, size=0):
        """initialize class"""

        if type(size) != int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """return area of square."""
        return (self.__size * self.__size)
