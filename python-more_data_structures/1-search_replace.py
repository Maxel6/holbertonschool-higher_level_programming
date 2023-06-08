#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if my_list == 0 or my_list is None:
        return None

    for num in my_list:
        if num == search:
            new_list.append(replace)
        else:
            new_list.append(num)
    return new_list
