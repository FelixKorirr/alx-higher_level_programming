#!/usr/bin/python3

def _subtract(y):
    _sub = 0
    my_list = max(y)

    for x in y:
        if my_list > x:
            _sub += x

    return (my_list - _sub)


def roman_to_int(roman_string):

    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    i = 0
    last = 0
    my_list = [0]

    for c in roman_string:
        for r in list_keys:
            if r == c:
                if rom_n.get(c) <= last:
                    i += _subtract(my_list)
                    my_list = [rom_n.get(c)]
                else:
                    my_list.append(rom_n.get(c))

                last = rom_n.get(c)

    i += _subtract(my_list)

    return (i)
