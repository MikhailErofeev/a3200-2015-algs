import math
n = int(input())
lst = [True for n in range(0, n + 1)]
lst[0] = False
lst[1] = False
def sieve(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        j = i ** 2
        while j <= n:
            lst[j] = False
            j = j + i
    return lst
lst = sieve(n)
print(lst)