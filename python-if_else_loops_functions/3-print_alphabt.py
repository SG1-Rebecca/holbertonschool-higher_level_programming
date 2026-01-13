#!/usr/bin/python3
for alphabt_ascii in range(97, 123):
    if alphabt_ascii == 113 or alphabt_ascii == 101:
        continue
    print("{}".format(chr(alphabt_ascii)), end="")
