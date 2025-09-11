#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary)
    for keys in sorted_dictionary:
        print("{}: {}".format(keys, a_dictionary[keys]))
