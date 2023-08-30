#!/usr/bin/python3

def magic_calculation(a, b):

    total = 0
    for x in range(1, 3):

        try:
            if x > a:
                raise Exception('Too far')
            else:
                total += a ** b / x
                
        except:
            total = b + a
            break

    return total
