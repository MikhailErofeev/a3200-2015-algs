def sieve(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return True

n = int(input())
a = [sieve(x) for x in range(1, n + 1)]
print(a)
