#!/usr/bin/env python3
import os
import sys

# warp directory run commands
wd = os.path.expanduser("~/.wdrc")

def usage():
    print("wd - warp directory")
    print("usage: ")
    print("\twd [alias] ; warp to alias")

def load():
    with open(wd) as fp:
        ln = fp.read().split()
        for l in ln:
            l = l.split("=")
            if sys.argv[1] == l[0]:
                if os.path.isdir(l[1]):
                    print(l[1])
                else:
                    sys.exit(2)

def main():
    # just check the count 
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    
    alias = sys.argv[1]
    if alias == "":
        return os.path.expanduser("~")

    load()

if __name__ == '__main__':
    main()
