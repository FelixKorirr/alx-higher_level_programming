#!/usr/bin/python3
"""define is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class
    Args:
        obj - object to check
        a_class - class to check from
    Return:
        True or False
    """

    if type(obj) is a_class:
        return True

    else:
        return False
