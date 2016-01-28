__author__ = 'Nikita Rybkin'
from sys import stdin, stdout


def area(arg):
    if len(arg) < 3:
        return 0
    peak = arg[0]
    ans = 0
    current = 0
    for i in range(1, len(arg)):
        if arg[i] < peak:
            current += (peak - arg[i])
        else:
            if current > ans:
                ans = current
            current = 0
            peak = arg[i]
    return ans


def bar_chart(arg):
    a = area(arg)
    arg.reverse()
    b = area(arg)
    return max(a, b)


if __name__ == "__main__":
    array = [int(i) for i in stdin.readline().split()]
    stdout.write(str(bar_chart(array)) + "\n")