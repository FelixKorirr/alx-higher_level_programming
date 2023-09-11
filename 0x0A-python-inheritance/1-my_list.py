#!/usr/bin/python3
"""define subclass MyList"""


class MyList(list):
    def print_sorted(self):
        """This sorts a list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
