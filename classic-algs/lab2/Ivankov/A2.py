import math


def sieve(n):
    list = [True for i in range(0, n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        k = 2 * i
        while k <= n:
            list[k] = False
            k += i
    list[0] = False
    list[1] = False
    return list


n = int(input())
list = sieve(n)
print(list)
