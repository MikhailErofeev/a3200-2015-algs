__author__ = 'Nikita Rybkin'

from sys import stdin, stdout


def palindrome(string):
    l = len(string)
    tmp = list()
    for i in range(l + 1):
        tmp.append([])
        for _ in range(l + 1):
            tmp[i].append(0)
    for i in range(l):
        for k in range(l):
            if string[i] == string[l - k - 1]:
                tmp[i + 1][k + 1] = tmp[i][k] + 1
            elif tmp[i][k + 1] < tmp[i + 1][k]:
                tmp[i + 1][k + 1] = tmp[i + 1][k]
            else:
                tmp[i + 1][k + 1] = tmp[i][k + 1]
    result = ''
    i = k = l
    while i > 0 and k > 0:
        if string[l - k] == string[i - 1]:
            result += string[i - 1]
            i -= 1
            k -= 1
        elif tmp[i - 1][k] >= tmp[i][k - 1]:
            i -= 1
        else:
            k -= 1
    return result


if __name__ == '__main__':
    string = stdin.readline()
    stdout.write(palindrome(string))
