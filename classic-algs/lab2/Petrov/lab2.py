from sys import stdin

def sieve(n):
    a = [True for i in range(n + 1)] 
    for i in range(2, int(math.sqrt(n)) + 1):
        j = i * 2
        while j <= n:
            a[j] = False
            j += i
    return a

n = int(stdin.readline())
ans = sieve(n)

for i in range(len(ans)):
    print(ans[i], end = ' ')
