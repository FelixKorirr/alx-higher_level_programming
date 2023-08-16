#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    result = sorted(a_dictionary.items())

    for i, j in result:
        print("{} : {}".format(i, j))
