#!/usr/bin/python3
import sys
if __name__ == "__main__":
    parse_arguments = sys.argv[1:]
    nb_arguments = len(parse_arguments)
    if nb_arguments == 0:
        print("0 arguments", end=".\n")
    elif nb_arguments == 1:
        print("1 argument", end=":\n")
    else:
        print("{} arguments: ".format(nb_arguments))
    for words in range(1, nb_arguments + 1):
        print("{}: {}".format(words, sys.argv[words]))
