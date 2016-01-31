__author__ = 'Nikita Rybkin'
import sys
from sys import stdin


def merge(a, b, c, d):
    n = c - b + 1
    m = d - c
    left_array = [None] * (n + 1)
    right_array = [None] * (m + 1)
    for i in range(n):
        left_array[i] = a[b + i]
    for i in range(m):
        right_array[i] = a[c + i + 1]
    left_array[n] = sys.maxint
    right_array[m] = sys.maxint
    i = 0
    j = 0
    for k in range(b, d + 1):
        if left_array[i] <= right_array[j]:
            a[k] = left_array[i]
            i += 1
        else:
            a[k] = right_array[j]
            j += 1


def insertion_sort(a, p, q):
    for j in range(p, q):
        key = a[j]
        i = j - 1
        while i >= p and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key


def m_sort(a, p, r, edge):
    if r - p < edge:
        insertion_sort(a, p, r)
    else:
        q = (p + r) / 2
        if (q - p) >= edge:
            m_sort(a, p, q, edge)
        else:
            insertion_sort(a, p, q + 1)
        if (r - q - 1) >= edge:
            m_sort(a, q + 1, r, edge)
        else:
            insertion_sort(a, q + 1, r + 1)
        merge(a, p, q, r)


def sort(a):
    if len(a) < 10:
        insertion_sort(a, 0, len(a))
    else:
        m_sort(a, 0, len(a) - 1, 10)


def merge_sort(array):
    lo = 0
    hi = len(array) - 1
    m_sort(array, lo, hi, 10)


if __name__ == "__main__":
    array = [int(s) for s in stdin.readline().split(' ')]
    sort(array)
    for p in array:
        sys.stdout.write(str(p) + ' ')