#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_list = len(my_list)
    for elements in range(len_list - 1, -1, -1):
        print("{}".format(my_list[elements]), end="\n")
