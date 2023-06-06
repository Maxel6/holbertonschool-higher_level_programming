#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = 0
    for i in range(0, len(matrix)):
        for y in matrix[i]:
            print("{:d}".format(y), end="")
            if idx != len(matrix[i]):
                print(" ", end="")
            idx += 1
        print()
        idx = 0
 