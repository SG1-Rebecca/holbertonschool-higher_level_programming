#!/usr/bin/python3
"""
Create or overwrite a file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written

    Args:
        filename (str): The name of the file to create or overwrite
        text (str): The text to overwrite to the file

    Returns:
        int: The number of characters written
    """
    if not filename:
        f = open(filename, 'x')
    else:
        with open(filename, 'w', encoding="UTF8") as fw:
            return fw.write(text)
