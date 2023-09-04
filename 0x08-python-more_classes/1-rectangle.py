#!/usr/bin/python3
"""define class"""


class Rectangle:
    """represent class"""

    def __init__(self, width=0, height=0):
        """initialize class"""

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """get/set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be integer")

        elif (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """get/set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be integer")

        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__height = value
