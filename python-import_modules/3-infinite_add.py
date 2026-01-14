#!/usr/bin/python3
import sys


def infinite_add():
    total_sum = 0
    len_nb = sys.argv[1:]
    for number in len_nb:
        total_sum += int(number)
    print(total_sum)


if __name__ == "__main__":
    infinite_add()
