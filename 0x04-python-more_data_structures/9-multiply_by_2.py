#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    key_val = list(new.keys())

    for x in key_val:
        new[x] *= 2

    return new
