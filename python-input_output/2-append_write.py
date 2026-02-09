#!/usr/bin/python3
"""
Module 2-append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and return the number of characters added

    Args:
        filename (str): The name of the file to append to
        text (str): The text to append to the file

    Returns:
        int: The number of characters added to the file
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as append_file:
            return append_file.write(text)
