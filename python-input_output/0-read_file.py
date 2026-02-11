#!/usr/bin/python3
"""
Module 0-read_file
"""


def read_file(filename=""):
    """
    Read a text file and print it to stdout

    Args:
        filename (str): The name of the file to read
    """
    with open(filename, encoding="utf-8") as read_file:
        print(read_file.read(), end="")
