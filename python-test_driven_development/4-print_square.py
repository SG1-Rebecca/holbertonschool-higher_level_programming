#!/usr/bin/python3
def print_square(size):
    """
    Print square with the character #

    Args:
        size: Size length of the square


    Return:
        Print the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for index in range(size):
        print("#" * size)
