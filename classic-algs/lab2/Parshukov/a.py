import math
def sieve(n):
    res = [True for i in xrange (n + 2)]

    for i in xrange (2, int (math.sqrt (n)) + 1):
        j = i + i
        while j <= n:
            res[j] = False
            j += i
            
    return res

n = int (raw_input ('input n: '))
res = sieve (n)

for i in xrange (2, n + 1):
    if res[i]:
        print i
