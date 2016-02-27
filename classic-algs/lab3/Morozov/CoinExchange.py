from sys import stdin, stdout
# coding=UTF-8
__author__ = 'vks'

money = int(stdin.readline())
coins = [int(val) for val in stdin.readline().split()]
count = len(coins)

dp = [[0 for j in range(count + 1)] for i in range(money + 1)]
for i in range(1, count + 1):
    dp[0][i] = 1

for i in range(1, money + 1):
    for j in range(1, count + 1):
        if j > 1:
            dp[i][j] = dp[i][j - 1]
        if i >= coins[j - 1]:
            dp[i][j] += dp[i - coins[j - 1]][j]

stdout.write(str(dp[money][count]) + "\n")
