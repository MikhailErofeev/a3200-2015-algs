from sys import stdin
from sys import stdout

def findcount(array):
    count = 0
    arr = sorted([i ** 2 for i in array])
    for i in range(2, len(arr)):
        left = 0
        right = i - 1
        while left < right:
            if arr[left] + arr[right] == arr[i]:
                count += 1
                break
            if arr[left] + arr[right] < arr[i]:
                left += 1
            else:
                right -= 1
    return count

if __name__ == '__main__':
    array = [int(i) for i in stdin.readline().split()]
    stdout.write(str(findcount(array)))
