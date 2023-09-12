#!/usr/bin/python3
"""Defines append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text to a file"""
    txt = ""
    with open(filename) as file:
        for line in file:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as files:
        files.write(txt)
