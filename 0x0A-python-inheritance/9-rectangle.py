#!/usr/bin/python3
"""defines Rectangle subclass"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent subclass"""

    def __init__(self, width, height):
        """Initializes subclass

        Args:width - width of rectangle
            height - height of rectangle
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates area of Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns string representation of an object"""
        return f"[Rectangle] {self.__width}/{self.__height}"
