#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):

    value = a_dictionary
    if value.get(key) is not None:

        del value[key]

    return (value)
