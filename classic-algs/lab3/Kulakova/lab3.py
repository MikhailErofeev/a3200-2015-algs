import sys
n = int(raw_input())
coins = sys.stdin.readline().split(' ')
for i in range (0, len(coins)):
    coins[i] = int(coins[i])
coins.sort()
steps = [0 for x in range (0, n + 1)]
steps[0] = 1
for x in range (0, len(coins)):
    if coins[x] <= n:
        for y in range (coins[x], n + 1):
            steps[y] = steps[y] + steps[y - coins[x]]
print steps[n]
