#!/usr/bin/python3
def print_list_integer(my_list=[]):
    len_int = len(my_list)
    for list_index in range(len_int):
        print("{:d}".format(my_list[list_index]), end="\n")
