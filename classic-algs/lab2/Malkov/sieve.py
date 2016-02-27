import math

def sieve(n):
    lst = [True] * n
    lst[0] = lst[1] = False
    prime = 2
    while prime < n:
        if lst[prime] == True:
            count = prime * 2
            while count < n:
                lst[count] = False
                count += prime
        prime += 1
    return lst

n = int(input())
result = sieve(n)
print(result)
