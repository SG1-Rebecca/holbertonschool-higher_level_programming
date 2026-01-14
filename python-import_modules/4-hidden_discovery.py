#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    p_names = dir()
    for name in sorted(p_names):
        if not name.startswith("__"):
            print(name)

