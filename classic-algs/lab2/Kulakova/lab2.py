import math
def sieve(n):
    array = [True for x in range (0, n + 1)]
    array [0] = False
    for i in range (2, int(math.sqrt(n)) + 1):
        a = 2 * i
        while a <= n:
            array [a] = False
            a += i
    return array

n = int(raw_input())
k = int(raw_input())
print sieve(n) [k]
