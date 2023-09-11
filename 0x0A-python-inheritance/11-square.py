#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a class Square."""

    def __init__(self, size):
        """Initializes class Square.

        Args:
            size : size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
