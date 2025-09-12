#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        nb_element = 0
        for index in range(x):
            print(my_list[index], end="")
            nb_element += 1
    except IndexError:
        pass # if index out of the range
    print()
    return nb_element