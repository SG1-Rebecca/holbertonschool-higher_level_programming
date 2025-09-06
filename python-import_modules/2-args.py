#!/usr/bin/python3
import sys
if __name__ == "__main__":
    nb_arguments = len(sys.argv)
    if nb_arguments == 0:
        print("0 arguments", sep='.')
    elif nb_arguments == 1:
        print("1: argument", sep=":")
        print("1: {}".format(nb_arguments))
    # else:
    #     print()
    for words in range(1, nb_arguments):
        print("{}: {}".format(words, sys.argv[words]))