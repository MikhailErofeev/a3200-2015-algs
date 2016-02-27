from sys import stdin

first_line = stdin.readline()
array = [int(s) for s in first_line.split()]


def qsort(a, l, r):
    left = l
    right = r
    middle = a[(left + right) / 2]

    while left <= right:
        while (a[left] < middle) and (left <= r):
            left += 1
        while (a[right] > middle) and (right >= l):
            right -= 1
        if left <= right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

    if right > l:
        qsort(a, l, right)
    if left < r:
        qsort(a, left, r)


qsort(array, 0, len(array) - 1)
print (array)
