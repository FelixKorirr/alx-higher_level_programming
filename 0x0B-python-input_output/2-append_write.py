#!/usr/bin/python3
"""Define append_write function"""


def append_write(filename="", text=""):
    """Appends string of the end of a file
    Args:
        filename: file to read content from
        text: string to append to file
    Returns: number of characters added
        """
    with open(filename, 'a', encoding='utf-8') as file:

        content = file.write(text)
        return content
