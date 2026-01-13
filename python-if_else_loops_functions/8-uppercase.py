#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for letter in str:
        if letter >= 'a' and letter <= 'z':
            str_upper += chr(ord(letter) - 32)
        else:
            str_upper += letter
    print("{}".format(str_upper), end="")
    print("{}".format(""))
