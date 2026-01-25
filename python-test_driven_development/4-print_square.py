#!/usr/bin/python3
"""
Module 4-print_square
"""


def print_square(size):
    """
    Print a square with the character #

    Args:
        size (int): The size of the square to be printed

    Return:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
