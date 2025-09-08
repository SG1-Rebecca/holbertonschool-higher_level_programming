#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_list = len(my_list)
    copy_mylist = my_list[:]
    if idx < 0:
        return my_list
    if idx >= len_list:
        return copy_mylist
    else:
        copy_mylist[idx] = element
        return copy_mylist
