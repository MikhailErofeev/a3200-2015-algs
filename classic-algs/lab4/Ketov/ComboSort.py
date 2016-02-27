from sys import stdin
from random import randint

# first_line = stdin.readline()
# array = [int(s) for s in first_line.split()]


def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while (i >= 0) and (arr[i] > key):
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def merge(left, right):
    l = 0
    r = 0
    arr = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr.append(left[l])
            l += 1
        else:
            arr.append(right[r])
            r += 1

    if l < len(left):
        for i in range(l, len(left)):
            arr.append(left[i])

    if r < len(right):
        for i in range(r, len(right)):
            arr.append(right[i])

    return arr


def comboSort(arr, k):
    if len(arr) < k:
        insertionSort(arr)
    else:
        left = comboSort(arr[0: int(len(arr) / 2)], k)
        right = comboSort(arr[int(len(arr) / 2): int(len(arr))], k)
        arr = merge(left, right)
    return arr


array = []
for i in xrange(0, 1000):
    array.append(randint(-1000, 1000))
print(array)

print (comboSort(array, 16))
