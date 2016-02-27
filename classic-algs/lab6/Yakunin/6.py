from sys import stdin
import radix_sort

arr = [int(n) for n in stdin.readline().split()]
for x in radix_sort.sort(arr):
    print(x, end=" ")
