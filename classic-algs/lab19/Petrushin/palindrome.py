__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

from sys import stdin as inp


def palindrome(string):
    length = len(string)
    tmp = list()
    for i in range(length + 1):
        tmp.append([])
        for _ in range(length + 1):
            tmp[i].append(0)
    for i in range(length):
        for j in range(length):
            if string[i] == string[length - j - 1]:
                tmp[i + 1][j + 1] = tmp[i][j] + 1
            elif tmp[i][j + 1] < tmp[i + 1][j]:
                tmp[i + 1][j + 1] = tmp[i + 1][j]
            else:
                tmp[i + 1][j + 1] = tmp[i][j + 1]
    result = ''
    i = length
    j = length
    while i > 0 and j > 0:
        if string[length - j] == string[i - 1]:
            result += string[i - 1]
            i -= 1
            j -= 1
        elif tmp[i - 1][j] >= tmp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return result


def main():
    string = inp.readline()
    print(palindrome(string))


if __name__ == '__main__':
    main()
