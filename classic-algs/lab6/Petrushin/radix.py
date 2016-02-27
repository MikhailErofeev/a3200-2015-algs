__author__ = 'Dmitry Petrushin'

from sys import stdin
from sys import stdout


def radix_sort(arr):
    if not arr:
        return []
    max_length = max([len(str(arr[i])) for i in range(len(arr))])
    for i in range(max_length):
        bucket = [[] for _ in range(10)]
        for j in arr:
            bucket[int((j / 10 ** i) % 10)].append(j)
        arr = []
        for section in bucket:
            arr.extend(section)
    return arr


def extended_radix_sort(arr):
    positive = radix_sort([elem for elem in arr if elem >= 0])
    negative = [-elem for elem in radix_sort([-elem for elem in arr if elem < 0])[::-1]]
    arr = negative + positive
    return arr


for elem in extended_radix_sort([int(elem) for elem in stdin.readline().split()]):
    stdout.write(str(elem) + " ")
