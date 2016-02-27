__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

from sys import stdin as inp
from sys import stdout as out


def find_count_of_triples(numbers):
    arr = sorted([i ** 2 for i in numbers])
    count = 0
    for i in range(2, len(arr))[::-1]:
        left = 0
        right = i - 1
        while left < right:
            if arr[left] + arr[right] == arr[i]:
                count += 1
                break
            elif arr[left] + arr[right] < arr[i]:
                left += 1
            else:
                right -= 1
    return count


if __name__ == '__main__':
    array = [int(i) for i in inp.readline().split()]
    out.write(str(find_count_of_triples(array)))
