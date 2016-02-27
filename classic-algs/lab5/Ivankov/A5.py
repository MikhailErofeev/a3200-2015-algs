__author__ = 'Laz.Go'

from sys import stdin
from sys import stdout
import random


def quicksort(array, begin, end):
    if end < begin + 2:
        return
    rand = random.Random()
    pivot = array[rand.randrange(begin, end)]
    left = begin
    right = end
    mid= begin
    while mid< right:
        if array[mid] < pivot:
            array[mid], array[left] = array[left], array[mid]
            left += 1
            mid+= 1
        elif array[mid] > pivot:
            right -= 1
            array[mid], array[right] = array[right], array[mid]
        elif array[mid] == pivot:
            mid+= 1
    quicksort(array, begin, left)
    quicksort(array, right, end)


def extended_quicksort(array):
    quicksort(array, 0, len(array))
    return array


for element in extended_quicksort([int(elem) for elem in stdin.readline().split(" ")]):
    stdout.write(str(element) + " ")