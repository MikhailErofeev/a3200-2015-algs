__author__ = 'Nikita Rybkin'

from sys import stdin, stdout


def dam_lev_dist(s1, s2):
    lines = list([len(s1) * [float('inf')],
                  len(s1) * [float('inf')]])
    for i in range(len(s2)):
        for j in range(len(s1)):
            if i == j == 0:
                if s1[0] == s2[0]:
                    lines[i][j] = 0
                else:
                    lines[i][j] = 1
            else:
                current, previous = lines[i % 2], lines[1 - i % 2]
                value = min(current[j - 1] + 1,
                            previous[j] + 1,
                            previous[j - 1] + int(not (s1[j] == s2[i])),
                            previous[j - 1] + int(not ((s1[j] == s2[i - 1]) and
                                                       (s2[i] == s1[j - 1]))))
                lines[i % 2][j] = value
    if len(s1) == len(s2) == 1:
        return 1
    else:
        return lines[1][len(s1) - 1]


if __name__ == '__main__':
    st1 = stdin.readline().rstrip('\n')
    st2 = stdin.readline().rstrip('\n')
    stdout.write(str(dam_lev_dist(st1, st2)))