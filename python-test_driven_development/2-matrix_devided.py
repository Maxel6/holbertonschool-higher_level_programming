#!/usr/bin/python3
"""Module that divides all elements of a matrix and return a new matrix
    Args:
        matrix (list of lists): two-dimensional data structure
        div (int, floats): divider
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a
    matrix by div and return a new matrix.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not (int or float):
        raise TypeError("div must be a number")

    new_matrix = [[round(element/div, 2) for element in row] for row in matrix]
    return new_matrix