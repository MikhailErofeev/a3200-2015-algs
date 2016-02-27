from sys import stdin
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
f = [0 for i in range(n + 1)]
f[0] = 1
 
for i in range(len(a)):
    for j in range(n):
        if f[j] and j + a[i] <= n:
            f[j + a[i]] += f[j]
           
print(f[n])
