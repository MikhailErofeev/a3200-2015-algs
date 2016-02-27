__author__ = 'alexkane'

from sys import stdin

first_line = stdin.readline()
n = int(first_line)
second_line = stdin.readline()
m = [int(s) for s in second_line.split(' ')]
index = len(m) - 1


def calculate(currentIndex, leftover):
    counter = 0

    if currentIndex == 0:
        if leftover > 0 and leftover % m[currentIndex] == 0:
            counter += 1
    else:
        while leftover >= 0:
            if leftover == 0:
                counter += 1
            else:
                newLeftover = leftover
                counter += calculate(currentIndex - 1, newLeftover)
            leftover -= m[currentIndex]
    return counter


print calculate(index, n)
