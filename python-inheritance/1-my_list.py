#!/usr/bin/python3
"""
Module 1-my_list
"""


class MyList(list):
    """
    Defines a class MyList that inherits from list.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
