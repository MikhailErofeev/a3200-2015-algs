from sys import stdin
maximum = stdin.readline()
coins = stdin.readline()
aCoins = []
end = 0
for i in xrange (0, coins.count(" ")):
    start = end
    end = coins.find(" ", end + 1, len(coins))
    if i == 0:
	start = -1
    aCoins.append(int(coins[start + 1:end]))
aCoins.append(int(coins[end + 1:len(coins)]))

def count(listOfCoins, lastIndexOfList, maximum):
    if maximum < 0:
        return 0
    elif maximum == 0:
        return 1
    elif lastIndexOfList < 0:
        return 0
    else:
        return count(listOfCoins, lastIndexOfList - 1, maximum) + count(listOfCoins, lastIndexOfList, maximum - listOfCoins[lastIndexOfList])

print count(aCoins, len(aCoins) - 1, int(maximum))

