#!/usr/bin/python3
def safe_print_integer(value):

    try:
        formatted = int(value)
        print(formatted)
        return True
    except ValueError:
        return False
