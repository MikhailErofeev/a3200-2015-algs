from sys import stdin

first_line = stdin.readline()
n = int(first_line)
second_line = stdin.readline()
m = [int(s) for s in second_line.split(' ')]
kindsOfCoins = len(m)


def numberOfVariants(n):
    return countFunction(n, kindsOfCoins)


def countFunction(n, kindsOfCoins):
    if n == 0:
        return 1
    elif n < 0 or kindsOfCoins == 0:
        return 0
    else:
        return countFunction(n, kindsOfCoins - 1) + countFunction(n - m[kindsOfCoins - 1], kindsOfCoins)



print numberOfVariants(n)
