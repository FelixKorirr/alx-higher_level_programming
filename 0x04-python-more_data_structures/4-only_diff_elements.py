#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    different_values = set_1 - set_2 | set_2 - set_1

    return different_values
