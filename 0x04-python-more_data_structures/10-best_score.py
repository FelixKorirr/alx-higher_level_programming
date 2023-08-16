#!/usr/bin/python3
def best_score(a_dictionary):

    value = a_dictionary

    if not value:
        return (None)

    return (max(value, key=value.get))
