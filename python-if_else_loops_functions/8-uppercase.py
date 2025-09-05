#!/usr/bin/python3
def uppercase(str):
    str_return = ""
    for letter in str:
        if letter >= 'a' and letter <= 'z':
            str_return += chr(ord('A') + (ord(letter) - ord('a')))
        else:
            str_return += letter
    print(str_return, end='')
    print()
