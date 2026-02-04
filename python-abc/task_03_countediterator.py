#!/usr/bin/python3
"""
Module task_03_countediterator
"""


class CountedIterator:
    """
    An iterator that keep track of the number of items iterated over.

    Attributes:
        iterator: The original iterator created from the input iterable.
        counter: A counter to keep track of the number of items iterated.
    """
    def __init__(self, some_iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            some_iterable: Description
        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """
        Get the current count of items iterated.

        Returns:
            int: The current value of the counter.
        """
        return self.counter

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            CountedIterator: The iterator object itself.
        """
        return self

    def __next__(self):
        """
        Fetch the next item from the original iterator
        and increment the counter.

        Raises:
            StopIteration: When there are no more items to iterate.

        Returns:
            The next item from the original iterator.
        """
        item = next(self.iterator)
        self.counter += 1
        return item
