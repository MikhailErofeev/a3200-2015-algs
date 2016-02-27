from sys import stdin
import random

def quicksort(arr, left, right):
    if right - left > 1:
        pt = arr[random.randint(left, right - 1)]
        lside = left
        rside = right
        i = left
        while i < rside:
            if arr[i] == pt:
                i += 1
            elif arr[i] < pt:
                arr[i], arr[lside] = arr[lside], arr[i]
                lside += 1
                i += 1
            else:
                rside -= 1
                arr[i], arr[rside] = arr[rside], arr[i]
        quicksort(arr, left, lside)
        quicksort(arr, rside, right)
    return arr

arr = [int(n) for n in stdin.readline().split(" ")]
random.seed()
for x in quicksort(arr, 0, len(arr)):
    print(x, end=" ")
