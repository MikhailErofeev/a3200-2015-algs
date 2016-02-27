from sys import stdin
import math
import sys


def i_digit(n, i):
    d = (abs(n)) % (10 ** (i + 1)) / (10 ** i)
    return d


def h_m_digits(n):
    t = int(math.log10(abs(n)) + 1)
    return t


def maximum(array):
    max = array[0]
    for i in range(1, len(array)):
        if max < array[i]:
            max = array[i]
    return max


def counting_sort(array, f):
    final = [0 for x in range(len(array))]
    order = [0 for x in range(10)]
    for j in range(len(array)):
        order[i_digit(array[j], f)] += 1
    for i in range(1, 10):
        order[i] += order[i - 1]
    j = len(array) - 1
    while j >= 0:
        order[i_digit(array[j], f)] -= 1
        final[order[i_digit(array[j], f)]] = array[j]
        j -= 1
    return final


def radix_sort(array):
    if not array:
        return []
    negatives = []
    positives = []
    for i in range(len(array)):
        if array[i] < 0:
            negatives.append(abs(array[i]))
        else:
            positives.append(array[i])
    n = h_m_digits(maximum(positives))
    m = h_m_digits(maximum(negatives))
    for i in range(0, n):
        positives = counting_sort(positives, i)
    for i in range(0, m):
        negatives = counting_sort(negatives, i)
    negatives.reverse()
    for i in range(len(negatives)):
        negatives[i] *= -1
    return negatives + positives


if __name__ == '__main__':
    elements = [int(s) for s in stdin.readline().split()]
    elements = radix_sort(elements)
    for i in elements:
        sys.stdout.write(str(i) + ' ')
