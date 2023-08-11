#!/usr/bin/python3

def magic_calculation(a, b):
    
    import magic_calculation_102 as result

    if a < b:
        c = result.add(a, b)
        for x in range(4, 6):
            c = result.add(c, x)
        return (c)

    else:
        return(result.sub(a, b))
