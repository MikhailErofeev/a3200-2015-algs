import math

def sieve(n):
    lst = [True for i in xrange(0, n + 1)] 
    for i in xrange(2, int(math.sqrt(n)) + 1):
        j = 2 * i
        while j <= n:
            lst[j] = False
            j += i
    lst[0] = False
    lst[1] = False
    return lst

n = int(raw_input())
lst = sieve(n)
print lst
