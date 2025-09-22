#!/usr/bin/python3
"""
Module class MyList
"""


class MyList(list):
    """
    A list class that inherits from list
    """
    def print_sorted(self):
        """
        Method that print the list sorted in ascending order
        """
        sort_list = sorted(self)
        print(sort_list)
