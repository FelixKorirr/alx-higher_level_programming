#!/usr/bin/python3
"""define MagicClass"""

import math


class MagicClass:
    """represent circle."""

    def __init__(self, radius=0):
        """initialize class"""

        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be an integer")
        self.__radius = radius

    def area(self):
        """return area of the class."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return circumference of class."""
        return (2 * math.pi * self.__radius)
