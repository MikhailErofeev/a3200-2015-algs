__author__ = 'Dmitry Petrsuhin'

import math


def is_simple(number):
    if number == 1:
        return False
    i = 2
    while i <= int(round(math.sqrt(number))):
        if number % i == 0:
            return False
        i += 1
    return True


def sieve(number):
    answer = []
    for i in range(1, number + 1):
        answer.append(is_simple(i))
    return answer


x = int(input())
print(sieve(x))
