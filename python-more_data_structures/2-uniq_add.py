#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set()
    result = 0
    for integers in my_list:
        if integers not in uniq_int:
            uniq_int.add(integers)
            result += integers
    return result
