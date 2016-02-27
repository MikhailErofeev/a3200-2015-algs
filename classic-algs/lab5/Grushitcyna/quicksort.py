from sys import stdin
import random
import sys


elem = [int(s) for s in stdin.readline().split()]

RandomSource = random.Random(2**64)


def partition(elem, left, right, pivot):
    low = i = left
    high = right - 1
    while i <= high:
        if elem[i] < pivot:
            elem[i], elem[low] = elem[low], elem[i]
            low += 1
            i += 1
        elif elem[i] > pivot:
            elem[i], elem[high] = elem[high], elem[i]
            high -= 1
        else:
            i += 1
    return low, high


def quick_sort(left, right):
    if right > left + 1:
        low, high = partition(elem, left, right, elem[RandomSource.randrange(left, right)])
        quick_sort(left, low)
        quick_sort(high + 1, right)
    return elem


quick_sort(0, len(elem))
for i in elem:
    sys.stdout.write(str(i) + ' ')

