#!/usr/bin/python3
"""define class"""


class Square:
    """Represent class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize class square"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the class"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the class"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area of the class"""
        return (self.__size * self.__size)

    def my_print(self):
        """print class with # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for y in range(0, self.__position[1])]
        for y in range(0, self.__size):
            [print(" ", end="") for i in range(0, self.__position[0])]
            [print("#", end="") for j in range(0, self.__size)]
            print("")
