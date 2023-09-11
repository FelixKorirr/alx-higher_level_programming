#!/usr/bin/python3
"""define is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or
    if the object is an instance of a class that inherited from,
    the specified class
    Args:
        obj - object to check
        a_class - class to check from
    Return:
        True or False
    """

    if isinstance(obj, a_class):
        return True

    else:
        return False
