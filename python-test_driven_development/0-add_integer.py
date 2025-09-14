#!/usr/bin/python3
def add_integer(a, b=98):
    """
    add_integer function

    Args:
        a: First integer
        b: Second integer, 

    Return:
        An integer: The addition of a and b

    """
    # Check if a and b is int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast float to integer
    a = int(a)
    b = int(b)

    return a + b
