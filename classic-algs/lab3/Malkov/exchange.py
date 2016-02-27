from sys import stdin

def exchange(n, coins):
    if n == 0:
        return 1
    elif n < 0 or len(coins) == 0:
        return 0
    else:
        return exchange(n, coins[1:amount]) + exchange(n - coins[0], coins)

n = int(stdin.readline())
coins = [int(coin) for coin in stdin.readline().split(' ')]
amount = len(coins)
print(exchange(n, coins))
