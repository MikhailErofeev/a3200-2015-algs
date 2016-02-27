from sys import stdin

first_line = stdin.readline()
m = int(first_line)


def sieve(n):
    arr = [True for i in range(n + 1)]
    i = 2
    for i in 0, 1:
        arr[i] = False

    while i * i <= n + 1:
        j = i * i

        if arr[i]:
            while j <= n + 1:
                arr[j] = False
                j = j + i
        i += 1

    return arr


array = sieve(m)
print(array)
