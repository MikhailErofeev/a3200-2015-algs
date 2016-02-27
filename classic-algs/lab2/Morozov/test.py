__author__ = 'vks'


def sieve(n):
    primes = [True for i in range(n + 1)]
    primes[0] = False
    primes[1] = False
    i = 2
    while (i ** 2 <= n):
        if (primes[i] == True):
            for j in range(i * i, n + 1, i):
                primes[j] = False
        i += 1
    return primes


n = int(input())
print(sieve(n))
