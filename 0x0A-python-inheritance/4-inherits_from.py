#!/usr/bin/python3
"""defines inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj - object to check
        a_class - class to check from
    Return:
        True or False
    """

    if issubclass(type(obj), a_class) and (type(obj) is not a_class):
        return True

    else:
        return False
