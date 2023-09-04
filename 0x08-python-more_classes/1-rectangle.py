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
        """get width of rectangle"""
        return f"_Rectangle__width: {self.__width}"

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be integer")

        elif (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """get height of rectangle"""
        return f"_Rectangle__height: {self.__height}"

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be integer")

        elif (value < 0):
            raise ValueError("width must be >= 0")

        self.__height = value
