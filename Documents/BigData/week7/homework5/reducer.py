#!/usr/bin/env python
import itertools
import operator
import sys


def parsePairs():
    for line in sys.stdin:
        words = line.strip('\n').strip('\t').translate(None, "()''").split(',')
        yield (int(words[0]), int(words[1]))


def reducer():
    for key, pairs in itertools.groupby(parsePairs(),
                                        operator.itemgetter(0)):
        count = sum(int(i[1]) for i in pairs)
        print '%i\t%i' % (key, count)

if __name__ == '__main__':
    reducer()
