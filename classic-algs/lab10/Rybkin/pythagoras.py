__author__ = 'Nikita Rybkin'
from sys import stdin, stdout


def triples_search(array):
    n = len(array)
    square = [0 for i in range(n)]
    counter = 0
    for i in range(n):
        square[i] = array[i] ** 2
    square.sort()
    a = len(square)
    j = 0
    while j < a:
        origin = square[j]
        i = j + 1
        while i < a and origin == square[i]:
            del square[i]
            a -= 1
        j += 1
    for i in range(2, a):
        r = i - 1
        l = 0
        while l < r:
            if square[l] + square[r] == square[i]:
                counter += 1
            if square[l] + square[r] < square[i]:
                l += 1
            else:
                r -= 1
    return counter


if __name__ == '__main__':
    els = [int(s) for s in stdin.readline().split()]
    stdout.write(str(triples_search(els)))