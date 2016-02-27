from sys import stdin


def exchanging(amount, coins):
    if amount == 0 or len(coins) == 0:
        return 0
    else:
        return rec_exchange(amount, len(coins))


def rec_exchange(m, n):
    if m == 0:
        return 1
    elif m < 0 or n == 0:
        return 0
    else:
        return rec_exchange(m, n - 1) + rec_exchange(m - coin_types[n - 1], n)


the_amount = stdin.readline()
coin_types = stdin.readline()
coin_types = coin_types.split()
coin_types = [int(i) for i in coin_types]
coin_types.sort()
the_amount = int(the_amount)
print exchanging(the_amount, coin_types)
