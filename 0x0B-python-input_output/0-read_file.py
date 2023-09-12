#!/usr/bin/python3
"""Define read_file function"""

def read_file(filename=""):
    """Reads content of a file
    Args:
        filename: file to read content from
    Returns: content
        """
    with open(filename, 'r',encoding='utf-8') as file:

        content = file.read()

    print(content)
