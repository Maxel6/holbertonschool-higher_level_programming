#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        b = 0
        for a in my_list:
            if b < a:
                b = a
        return b
    return None
