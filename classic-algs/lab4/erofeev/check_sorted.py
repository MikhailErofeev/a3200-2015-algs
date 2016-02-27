

from sys import stdin

__author__ = 'erofeev'

line = stdin.readline()
input = [int(s) for s in filter(None, line.split())]

asc = all(input[i] <= input[i + 1] for i in xrange(len(input) - 1))
print asc
if not asc:
    for i in xrange(len(input) - 1):
        if not input[i] <= input[i + 1]:
            print i,'/',len(input)
            break
desc = all(input[i] >= input[i + 1] for i in xrange(len(input) - 1))
print desc
if not desc:
    for i in xrange(len(input) - 1):
        if not input[i] > input[i + 1]:
            print i,'/',len(input)
            break