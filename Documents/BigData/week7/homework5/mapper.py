#!/usr/bin/env python
import sys


def mapper():
    for line in sys.stdin:
        words = line.strip().split(',')
        # if the remainder is more than 30 sec, add one more min
        if int(words[2]) % 60 >= 30:
            print (int(words[2]) / 60 + 1, 1)
        else:
            print (int(words[2]) / 60, 1)

if __name__ == '__main__':
    mapper()
