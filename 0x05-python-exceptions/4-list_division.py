#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    new = []
    for x in range(0, list_length):
        try:
            divider = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            divider = 0

        except ZeroDivisionError:
            print("division by 0")
            divider = 0

        except IndexError:
            print("out of range")
            divider = 0

        finally:
            new.append(divider)
    return (new)
