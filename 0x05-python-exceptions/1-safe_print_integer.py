#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int(value)
        print("{}".format(value))
        return value
    except ValueError:
        return False
