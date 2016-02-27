from sys import stdin

def change(cur, money):
    if money != 0:
        if money < 0 or len(cur) == 0:
            return 0
        else:
            return change(cur[1:len(cur)], money) + change(cur, money - cur[0])
    else:
        return 1
    
money = int (stdin.readline()) 
curList = stdin.readline()
print(change([int(n) for n in curList.split(" ")], money))
