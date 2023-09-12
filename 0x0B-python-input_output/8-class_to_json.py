#!/usr/bin/python3
"""Defines class_to_json function"""


def class_to_json(obj):
    """Return the dictionary representation with a simple data structure"""
    return obj.__dict__
