#!/usr/bin/python3
import sys
if __name__ == "__main__":
    parse_arguments = sys.argv[1:]
    nb_arguments = len(parse_arguments)
    if nb_arguments == 0:
        print("0 arguments", sep='.')
    elif nb_arguments == 1:
        print("1: argument", sep=":")
        print("1: {}".format(parse_arguments))
    else:
         print("{} arguments: ".format(nb_arguments))
    for words in range(1, nb_arguments):
        print("{}: {}".format(words, sys.argv[words]))