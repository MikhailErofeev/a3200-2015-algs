from sys import stdin, stdout

def countMin(n):
    flag = 0
    while n >= 64:
        flag += n & 1
        n >>= 1
    return n + flag

def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i > 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr
            
def combineSort(arr):
    if len(arr) < minrun:
        arr = insertionSort(arr)
    else:
        arr[0:int(len(arr) / 2) + 1] = combineSort(arr[0:int(len(arr) / 2) + 1])
        arr[int(len(arr) / 2):len(arr)] = combineSort(arr[int(len(arr) / 2):len(arr)])
        arr = merge(arr, 0, int(len(arr) / 2) + 1, len(arr))
    return arr

def merge(arr, left, mid, right):
    it1 = 0
    it2 = 0
    result = [0] * (right - left)
  
    while left + it1 < mid and mid + it2 < right:
        if arr[left + it1] < arr[mid + it2]:
            result[it1 + it2] = arr[left + it1]
            it1 += 1
        else:
            result[it1 + it2] = arr[mid + it2]
            it2 += 1
  
    while left + it1 < mid:
        result[it1 + it2] = arr[left + it1]
        it1 += 1
  
    while mid + it2 < right:
        result[it1 + it2] = arr[mid + it2]
        it2 += 1

    return result
        
arr = [int(elem) for elem in stdin.readline().split(' ')]
n = len(arr)
minrun = countMin(n)
arr = combineSort(arr)
stdout.write(" ".join(map(str, arr)))
