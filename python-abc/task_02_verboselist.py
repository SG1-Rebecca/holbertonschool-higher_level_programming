#!/usr/bin/python3
"""
Module task_02_verboselist
"""


class VerboseList(list):
    """
    A VerboseList class that extends the built-in list class
    """
    def append(self, item):
        """
        Append an item to the list and print a message
        """
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, item):
        """
        Extend the list and print a message
        """
        super().extend(item)
        print(f"Extended the list with {[len(item)]} items.")

    def remove(self, value):
        """
        Remove a value from the list and print a message
        """
        print(f"Removed {[value]} from the list.")
        super().remove(value)

    def pop(self, index=-1):
        """
        Pop an item from the list and print a message
        """
        poped_value = super().pop(index)
        print(f"Popped {[poped_value]} from the list.")
        return poped_value
