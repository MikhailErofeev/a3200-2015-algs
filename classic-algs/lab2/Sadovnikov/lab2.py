__author__ = 'vmath'

def eratosthene(n):
    array = [True for x in range(n+1)]
    array[0] = False
    array[1] = False
    for i in xrange(2,n+1):
        if i*i <= n:
            if array[i]:
                j = i*i
                while j <= n:
                    array[j] = False
                    j += i
    return array

print eratosthene(17)


