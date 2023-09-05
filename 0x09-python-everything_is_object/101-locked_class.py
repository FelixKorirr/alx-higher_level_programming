#!/usr/bin/python3
"""Defines locked class."""


class LockedClass:
    """
    Prevents the user from instantiating new lockedclass attributes
    for anything but the attribute 'first_name'
    """

    __slots__ = ["first_name"]
