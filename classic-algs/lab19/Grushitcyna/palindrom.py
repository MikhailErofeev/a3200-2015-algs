def find_palindrom(s):
    j = len(s)
    matrix = [[0 for k in xrange(j)] for i in xrange(j)]
    matrix2 = [[(0, 0) for k in xrange(j)] for i in xrange(j)]
    for m in xrange(j):
        matrix[m][m] = 1
    for l in xrange(1, j + 1):
        for m in xrange(j - l):
            if s[m] == s[m + l]:
                matrix[m + l][m] = matrix[m + l - 1][m + 1] + 2
                matrix2[m + l][m] = (m + l - 1, m + 1)
            else:
                if matrix[m + l - 1][m] > matrix[m + l][m + 1]:
                    matrix[m + l][m] = matrix[m + l - 1][m]
                    matrix2[m + l][m] = (m + l - 1, m)
                else:
                    matrix[m + l][m] = matrix[m + l][m + 1]
                    matrix2[m + l][m] = (m + l, m + 1)
    return matrix[j - 1][0], max_polindrom(matrix, matrix2, s)


def max_polindrom(matrix, matrix2, s):
    result = ''
    j = len(s) - 1
    i = 0
    while j > len(s)/2:
        a, b = matrix2[j][i]
        if matrix[j][i] != matrix[a][b]:
            result += s[i]
        i = b
        j = a
    return result


print(find_palindrom('arosaupalanalapuasora'))
