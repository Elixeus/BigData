#!/usr/bin/env python
import itertools
import operator
import sys


def parsePairs():
    for line in sys.stdin:
        words = line.strip('\t').strip('\n').translate(None, "()''").split(',')
        yield (int(words[0]), int(words[1]))


def reducer2():
    minutes = {}
    cumSum = 0
    total = 0
    for key, pairs in itertools.groupby(parsePairs(),
                                        operator.itemgetter(0)):
        minutes[int(key)] = [int(i[1]) for i in pairs][0]
    total = sum(minutes.values())
    for i in sorted(minutes.keys()):
        cumSum += minutes[i]
        if cumSum >= total / 2.0:
            print 'The median is {0} minutes'.format(i)
            break
if __name__ == '__main__':
    reducer2()
