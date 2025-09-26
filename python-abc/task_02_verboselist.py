#!/usr/bin/python3
"""
Module containing VerboseList class
"""


class VerboseList(list):
    """
    VerboseList class that inherits from list
    """
    def append(self, item):
        """
        Append item at the end of the list and print a notification
        """
        super().append(item)
        print(f"Added [{item}] to the list")

    def extend(self, iterable):
        """
        Extend the list with elements from iterable and print notification
        """
        len_list = len(self)
        super().extend(iterable)
        nb_item_added = len(self) - len_list
        print(f"Extended the list with [{nb_item_added}] items.")

    def remove(self, element):
        """
        Remove the first element from the list and print a notification
        """
        if element not in self:
            raise ValueError("Value not in the list")
        super().remove(element)
        print(f"Removed [{element}] from the list.")

    def pop(self, index=-1):
        """
        Remove the item a the given index and print a notification
        If not specified, remove the last item
        Raises:
            IndexError: If the list is empty
        """
        position = len(self)
        if position == 0:
            raise IndexError("Pop from an empty list")

        item = self[index]
        super().pop(index)
        print(f"Popped [{item}] from the list.")
