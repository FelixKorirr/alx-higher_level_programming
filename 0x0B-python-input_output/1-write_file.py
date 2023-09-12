#!/usr/bin/python3
"""Defines write_file function"""


def write_file(filename="", text=""):
    """Writes content to a file
    Args:
        filename: file to write content to
        text: Text to write
    Returns: number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:

        content = file.write(text)
    return content
