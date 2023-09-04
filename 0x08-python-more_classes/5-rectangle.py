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
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """get/set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Calculates perimeter of the rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Represents the rectangle with the # character."""
        if (self.__width == 0) or (self.__height == 0):
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
