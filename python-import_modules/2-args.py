#!/usr/bin/python3
import sys
if __name__ == "__main__":
    parse_arguments = sys.argv[1:]
    nb_arguments = len(parse_arguments)
    if nb_arguments == 0:
        print("0 arguments.")
    elif nb_arguments == 1:
        print("1 argument:")
    else:
        print(f"{nb_arguments} arguments: ")
    for n, display_args in enumerate(parse_arguments):
        print(f"{n + 1}: {display_args}")
