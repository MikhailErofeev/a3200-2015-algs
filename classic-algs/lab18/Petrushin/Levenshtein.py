__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

from sys import stdin as inp


def distance(a, b):
    lines = list([len(a) * [float('inf')],
                  len(a) * [float('inf')]])
    for i in range(len(b)):
        for j in range(len(a)):
            if i == j == 0:
                # xor as lambda-function
                lines[0][0] = (lambda x, y: 0 if x == y else 1)(a[0], b[0])
            else:
                current, previous = lines[i % 2], lines[1 - i % 2]
                value = min(current[j - 1] + 1,
                            previous[j] + 1,
                            previous[j - 1] + int(not (a[j] == b[i])),
                            previous[j - 1] + int(not ((a[j] == b[i - 1]) and
                                                       (b[i] == a[j - 1]))))
                lines[i % 2][j] = value
    if len(a) == len(b) == 1:
        return 1
    else:
        return lines[1][len(a) - 1]


def main():
    a = inp.readline().rstrip('\n')
    b = inp.readline().rstrip('\n')
    print(distance(a, b))


if __name__ == '__main__':
    main()
