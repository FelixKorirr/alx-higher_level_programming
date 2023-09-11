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
