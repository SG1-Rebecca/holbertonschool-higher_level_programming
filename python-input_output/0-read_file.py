#!/usr/bin/python3
"""
Reads and prints a file
"""


def read_file(filename=""):
    """
    Read a text file and print to stdout

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        read_content = f.read()
    print(read_content)
