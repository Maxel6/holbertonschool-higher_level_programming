#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == 0 or my_list is None:
        return None
    return sum(set(my_list))
