#!/usr/bin/python3
"""Defines read_file function"""

def read_file(filename=""):
    """Reads the content of a file
    Args:
        filename: file to read content from
    Returns: content of the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:

            content = file.read(filename)
            print(content)

    except FileNotFoundError:
        print("File {filename} does not exist!")

    except Exception as exp:
        print(f"Error occurred on {str(exp)}")
