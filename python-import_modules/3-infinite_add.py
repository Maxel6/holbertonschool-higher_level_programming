#!/usr/bin/python3
import sys
if __name__ == '__main__':
    res = 0
    argv = sys.argv[1:]
    for x in argv:
        res = res + int(x)
    print("{}".format(res))
