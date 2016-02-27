__author__ = 'Dmitry Petrushin'

from sys import stdin
from sys import stdout
import random


def quicksort(arr, begin, end):
    if end < begin + 2:
        return
    rand = random.Random()
    pivot = arr[rand.randrange(begin, end)]
    lt = begin
    gt = end
    i = begin
    while i < gt:
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            gt -= 1
            arr[i], arr[gt] = arr[gt], arr[i]
        elif arr[i] == pivot:
            i += 1
    quicksort(arr, begin, lt)
    quicksort(arr, gt, end)


def extended_quicksort(arr):
    quicksort(arr, 0, len(arr))
    return arr


for element in extended_quicksort([int(elem) for elem in stdin.readline().split(" ")]):
    stdout.write(str(element) + " ")
