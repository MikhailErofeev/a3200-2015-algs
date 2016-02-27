from sys import stdin

first_line = stdin.readline()
n = int(first_line)
second_line = stdin.readline()
array = [int(s) for s in second_line.split()]

m = len(array)


def count(n, m):
    if n == 0:
        return 1
    elif (n < 0) or (m < 0):
        return 0
    else:
        return count(n, m - 1) + count(n - array[m - 1], m)


print count(n, m - 1)
