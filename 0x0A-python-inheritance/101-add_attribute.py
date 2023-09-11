#!/usr/bin/python3
"""Function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object

    Args:
        obj : object to add an attribute to.
        att : name of the attribute to add to obj.
        value : value of att.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
