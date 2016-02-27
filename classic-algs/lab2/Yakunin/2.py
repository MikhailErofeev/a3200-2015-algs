import math

def simpleCheck(inp):
    i = 2
    while i <= int(round(math.sqrt(inp))):
        if inp % i == 0:
            return False
        i += 1
    return True

n = int(input())
anslist = [False]
for i in range(2, n + 1):
    anslist.append(simpleCheck(i))
print(anslist)
