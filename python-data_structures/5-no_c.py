#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for letters in my_string:
        if ord(letters) != 67 and ord(letters) != 99:
            new_string += letters
    return new_string
