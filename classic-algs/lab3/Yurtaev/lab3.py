from sys import stdin

def get(i, j):
    if (j == -1):
        return 1
    if (i >= 0) and (j >= 0) and (dp[i][j] != -1):
            return dp[i][j]
    return 0

n = int(stdin.readline())
str_coins = stdin.readline().split()
coins = [int(str_coins[i]) for i in range(0, len(str_coins))]
dp = [[-1 for j in range(0, n)] for i in range(0, len(coins))]
for i in range(0, len(coins)):
    for j in range(0, n):
        dp[i][j] = get(i - 1, j) + get(i, j - coins[i])
print get(len(coins) - 1, n - 1)
