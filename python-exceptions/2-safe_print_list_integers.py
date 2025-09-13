#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_element = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            nb_element += 1
        except (TypeError, ValueError):
            pass # other type of value in the list skipped in silence
    print()
    return nb_element
