#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for integers in matrix:
        def square_value(x):
            return x ** 2
        square_int = list(map(square_value, integers))
        new_matrix.append(square_int)
    return new_matrix
