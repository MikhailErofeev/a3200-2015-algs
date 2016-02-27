import math

def radixsort(array):
    if len(array) == 0:
        return array
    min = array[0]
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    for i in range(len(array)):
        array[i] -= min
    maxLen = -1
    for n in array:
        if (n == 0):
            numLen = 0
        else:
            numLen = int(math.log10(n)) + 1
        if numLen > maxLen:
            maxLen = numLen
    buckets = [[] for i in range(0, 10)]
    for digit in range(0, maxLen):
        for n in array:
            buckets[n // 10 ** digit % 10].append(n)
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    for i in range(len(array)):
        array[i] += min
    return array
