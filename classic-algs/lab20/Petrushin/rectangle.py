__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

from sys import stdin as inp


def rectangles(lengths):
    n_max = 10 ** 6 + 2
    sticks = [0 for _ in range(n_max)]
    tmp = list()
    for length in lengths:
        sticks[length] += 1
    for i in range(n_max - 2, 1, -1):
        for _ in range((sticks[i + 1] % 2 + sticks[i]) // 2):
            tmp.append(i)
        if sticks[i] > 0:
            sticks[i] += sticks[i + 1] % 2
    result = 0
    for i in range(1, len(tmp), 2):
        result += tmp[i - 1] * tmp[i]
    return result


def main():
    N = inp.readline()
    lengths = list(map(int, inp.readline().split()))
    print(rectangles(lengths))


if __name__ == '__main__':
    main()
