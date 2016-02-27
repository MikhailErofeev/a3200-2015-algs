__author__ = 'Nikita Rybkin'
import sys
import random


def split(array, left, right):
    idx = random.randint(left, right)
    array[left], array[idx] = array[idx], array[left]
    x = array[left]
    less = left
    greater = right
    j = left
    while j <= greater:
        if array[j] < x:
            array[less], array[j] = array[j], array[less]
            less += 1
            j += 1
        elif array[j] > x:
            array[greater], array[j] = array[j], array[greater]
            greater -= 1
        else:
            j += 1
    return less, greater


def sort(array, left, right):
    if left < right:
        less, greater = split(array, left, right)
        sort(array, left, less - 1)
        sort(array, greater + 1, right)


def quick_sort(array):
    left = 0
    right = len(array) - 1
    sort(array, left, right)


if __name__ == "__main__":
    a = [int(s) for s in sys.stdin.readline().split()]
    quick_sort(a)
    for i in a:
        sys.stdout.write(str(i) + ' ')