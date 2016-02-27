from sys import stdin
n = int(stdin.readline())
money = [int(i) for i in stdin.readline().split()]
elem = len(money)
tabl = []
for i in range(elem + 1):
    tabl.append([])
    for j in range(n + 2):
        tabl[i].append(0)
for i in range(1, elem + 1):
    tabl[i][0] = money[i - 1]
for i in range(1, elem + 1):
    tabl[i][1] = 1
k = 0
for j in range(1, n + 2):
    tabl[0][j] = k
    k = k + 1
for j in range(2, n + 2):
    if tabl[0][j] % tabl[1][0] == 0:
        tabl[1][j] = 1
for i in range(2, elem + 1):
    for j in range(2, n + 2):
        if tabl[0][j] < tabl[i][0]:
            tabl[i][j] = tabl[i - 1][j]
        else:
            tabl[i][j] = tabl[i - 1][j] + tabl[i][j - tabl[i][0]]
print(tabl[elem][n + 1])