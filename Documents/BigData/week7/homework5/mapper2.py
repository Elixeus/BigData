#!/usr/bin/env python
import sys


def mapper2():
    for line in sys.stdin:
        words = line.strip().split()
        print (words[0], words[1])


if __name__ == '__main__':
    mapper2()
