from sys import stdin, stdout
import random

def quick_sort(start, end):
    if end > start + 1:
        left, right = partition(start, end, arr[random.randint(start, end)])
        quick_sort(start, left)
        quick_sort(right + 1, end)
    return arr
    
def partition(start, end, pivot):
    left = i = start
    right = end - 1
    while i <= right:
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1
    return left, right
    
arr = [int(s) for s in stdin.readline().split()]
quick_sort(0, len(arr))
stdout.write(" ".join(map(str, arr)))
