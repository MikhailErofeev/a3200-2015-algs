__author__ = 'Nikita Rybkin'
import sys


def ith_digit(number, i):
    return (number % (10 ** (i + 1))) // (10 ** i)


def count_sort(a, b, k):
    digits = [0 for i in range(10)]
    for i in a:
        idx = ith_digit(i, k)
        digits[idx] += 1
    for i in range(1, 10):
        digits[i] += digits[i - 1]
    for i in range(len(a) - 1, -1, -1):
        idx = ith_digit(a[i], k)
        b[digits[idx] - 1] = a[i]
        digits[idx] -= 1


def number_of_digits(number):
    counter = 0
    while number > 0:
        counter += 1
        number //= 10
    return counter


def radix_sort(array):
    if len(array) == 0:
        return array
    min_number = min(array)
    for i in range(len(array)):
        array[i] -= min_number
    max_length = number_of_digits(max(array))
    b = [0 for i in range(len(array))]
    for i in range(max_length + 1):
        count_sort(array, b, i)
        array, b = b, array
    for i in range(len(array)):
        array[i] += min_number
    return array


if __name__ == "__main__":
    array = [int(i) for i in sys.stdin.readline().split()]
    array = radix_sort(array)
    for i in array:
        sys.stdout.write(str(i) + ' ')