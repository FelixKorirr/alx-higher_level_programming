#!/usr/bin/python3

def search_replace(my_list, search, replace):
    search = 1
    replace = 89

new = []

for i in my_list:

    if i == search:
        new.append(replace)
    else:
        new.append(i)
print(new)
