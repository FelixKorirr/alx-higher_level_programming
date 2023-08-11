#!/usr/bin/python3

if __name__ == "__main__":
    
    import calculator_1 as new

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, new.add(a, b)))
    print("{} - {} = {}".format(a, b, new.sub(a, b)))
    print("{} * {} = {}".format(a, b, new.mul(a, b)))
    print("{} / {} = {}".format(a, b, new.div(a, b)))
