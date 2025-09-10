#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = set_1.difference(set_2)
    diff_set_2 = set_2.difference(set_1)
    return diff_set.union(diff_set_2)
