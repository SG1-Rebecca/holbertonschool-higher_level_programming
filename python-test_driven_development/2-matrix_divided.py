#!/usr/bin/python3
"""
Module 2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div

    Args:
        matrix (list of lists of int/float): The matrix to be divided
        div (int/float): The divisor

    Returns:
        list of lists of float: New matrix with divided values
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(row, list) and row for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(element / div, 2) for element in row] for row in matrix]
