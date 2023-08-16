#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    key_val = list(a_dictionary.keys())

    for i in key_val:

        if value == a_dictionary.get(i):
            del a_dictionary[i]

    return (a_dictionary)
