#!/usr/bin/python3
ascii_alphabt = 97
for ascii_alphabt in range(97, 123):
    if ascii_alphabt == 101:
        continue
    if ascii_alphabt == 113:
        continue
    print(chr(ascii_alphabt), end="")
