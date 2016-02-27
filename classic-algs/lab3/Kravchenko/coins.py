from sys import stdin, stdout
first_line = stdin.readline()
second_line = stdin.readline()
n = int(first_line)
a = [int(j) for j in second_line.split()]
a.sort()
length = len(a) - 1


def glasgow(number, length):
    s = 0
    if number == 0:
        s = 1
    elif (number < 0) or (length < 0):
        s = 0
    else:
        while number >= 0:
            s += glasgow(number, length - 1)
            number -= a[length]
    return s


stdout.write(str(glasgow(n, length)))
