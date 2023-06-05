#!/usr/bin/python3
import sys
res = 0
argv = sys.argv[1:]
argc = len(argv)
for x in argv:
    res = res + int(x)
print("{}".format(res))
