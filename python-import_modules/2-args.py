#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argv = sys.argv[1:]
    argc = len(argv)
    sentence = "arguments."
    if argc == 1:
        sentence = "argument:"
    if argc > 1:
        sentence = "arguments:"
    print("{} {}".format(argc, sentence))
    for i in range(argc):
        print("{}: {}".format(i + 1, argv[i]))
