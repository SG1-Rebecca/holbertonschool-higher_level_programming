#!/usr/bin/python3
"""
"""
def read_file(filename=""):
    """
    Read a text file and print to stdout
    """
    with open(filename, 'r', encoding= "UTF8") as f:
        read_content = f.read()
        print(read_content)
