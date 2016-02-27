import math

def sieve(x):

    a = [True for i in xrange(x + 1)]
    a[0] = False
    a[1] = False
    for i in xrange(2, int(x ** 0.5) + 1):
        if a[i]:
            j = 2 * i
            while j <= x:
	        a[j] = False
	        j += i
    return a

x = int (raw_input('x = '))
list = sieve(x)
print list
