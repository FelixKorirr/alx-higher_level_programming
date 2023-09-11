#!/usr/bin/python3
"""defines BaseGeometry Class"""


class BaseGeometry:
    """Represents class"""
    def __init__(self):
        """Initializes class"""
    
    def area(self):
        """Method that raises an exception"""
        raise Exception("Area() is not implemented")
    
    def integer_validator(self, name, value):
        self.name = name
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
        self.value = value
