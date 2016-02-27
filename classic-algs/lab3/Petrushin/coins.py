__author__ = 'Dmitry Petrushin'

from sys import stdin


def change(summ, coins):
    if summ == 0:
        return 1
    else:
        if summ < 0 or len(coins) == 0:
            return 0
        else:
            return change(summ, coins[1:len(coins)]) + change(summ - coins[0], coins)


amount = int(stdin.readline())
coin = stdin.readline()
print(change(amount, [int(n) for n in coin.split(" ")]))
