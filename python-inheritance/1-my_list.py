#!/usr/bin/python3
"""
Module 1-my_list
"""


class MyList(list):
    """
    A MyList class that inherits from list

    Args:
        list (list): The built-in list class
    """
    def print_sorted(self):
        """
        Prints the list in sorted order
        """
        print(sorted(self))
