#!/usr/bin/python3
"""
Function that
add two integer

"""


def add_integer(a, b=98):
    """
    return the sum of a + b
    """
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        sum = int(a) + int(b)
        return sum
    except Exception as e:
        return e

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
  
