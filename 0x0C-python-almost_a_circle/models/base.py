#!/usr/bin/python3
"""Define base superclass"""


class Base:
    """Represent superclass"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
