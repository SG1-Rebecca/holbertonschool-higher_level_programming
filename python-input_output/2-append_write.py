#!/usr/bin/python3
"""
Appends a string to the end of a text file
"""


def append_write(filename="", text=""):
    """
    Append a string to a text file and returns the number of characters written

    Args:
        filename (str): The name of the file to append
        text (str): The text to append to the file

    Returns:
        int: The number of characters written
    """
    if not filename:
        f = open(filename, 'x')
    else:
        with open(filename, 'a', encoding="UTF8") as fa:
            return fa.write(text)
