import math


def sieve(n):
    if n == 1:
        return [False]
    mas = [True for i in range(n)]
    mas[0] = False
    for i in range(1, int(math.sqrt(n))+1):
        if mas[i]:
            j = (i + 1)*(i + 1)
            while j <= n:
                mas[j-1] = False
                j = j + i + 1
    return mas

v = int(input())
print sieve(v)
