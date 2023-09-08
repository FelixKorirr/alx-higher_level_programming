#!/usr/bin/python3
"""module to find the maximum integer in a list"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integer"""
    if len(list) == 0:
        return None
        
    value = list[0]
    x = 1
    while x < len(list):
        if list[x] > value:
            value = list[x]
        x += 1
    return value
