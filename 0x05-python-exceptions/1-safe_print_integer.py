#!/usr/bin/python3
def safe_print_integer(value):

    try:
        result = "{:d}".format(value)
        print(result)

        return True

    except ValueError:
        return False
