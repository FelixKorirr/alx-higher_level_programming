#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    my_dict = a_dictionary
    
    checker = my_dict.get(key)

    if checker is None:
        my_dict[key] = value

    else:
        my_dict[key] = value
