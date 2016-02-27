def sieve(n):
    myList = [True for i in range(n+1)]
    i = 2
    while i*i<n+1:
        if (myList[i] == True):
            for j in range(i*i, n+1, i):
                    myList[j] = False
        i+=1            
    for i in 0,1:
        myList[i] = False
    return myList
n = int(input())
myList = sieve(n)
print(myList)
