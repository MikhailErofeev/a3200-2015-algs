__author__ = 'Laz.Go'

from sys import stdin
from sys import stdout


def radixSort(array):
    if not array:
        return []
    maxLenght = max([len(str(array[i])) for i in range(len(array))])
    for i in range(maxLenght):
        box = [[] for _ in range(10)]
        for j in array:
            box[int((j / 10 ** i) % 10)].append(j)
        array = []
        for section in box:
            array.extend(section)
    return array


def eRadixSort(arr):
    pos = radixSort([elem for elem in arr if elem >= 0])
    neg = [-elem for elem in radixSort([-elem for elem in arr if elem < 0])[::-1]]
    arr = neg + pos
    return arr


for elem in eRadixSort([int(elem) for elem in stdin.readline().split()]):
    stdout.write(str(elem) + " ")