__author__ = 'Laz.Go'

from sys import stdin


kol = int(stdin.readline())
coins = stdin.readline()

def razmen(sum, coin):
    if sum == 0:
        return 1
    else:
        if sum < 0 or len(coin) == 0:
           return 0
        else:
           return razmen(sum, coin[1:len(coin)]) + razmen(sum - coin[0], coin)


print(razmen(kol, [int(n) for n in coins.split(" ")]))
