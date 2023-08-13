#!/usr/bin/python3
def no_c(my_string):

    value = ('c', 'C')
    new_list = ''.join([item for item in my_string if item not in value])

    return new_list
