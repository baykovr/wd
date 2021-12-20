#!/usr/bin/env python3
import os
import sys

rc = os.path.expanduser("~/.wdrc")

def main():
    if len(sys.argv) != 2:
        sys.exit(0)
    
    if sys.argv[1] == "":
        return os.path.expanduser("~")

    if os.path.isfile(rc):
        with open(rc) as fp:
            ln = fp.read().split()
            for l in ln:
                l = l.split("=")
                if sys.argv[1] == l[0]:
                    if os.path.isdir(l[1]):
                        print(l[1])
                    else:
                        sys.exit(2)
if __name__ == '__main__':
    main()
