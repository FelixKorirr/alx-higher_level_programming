#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """prints square with the # character"""
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
