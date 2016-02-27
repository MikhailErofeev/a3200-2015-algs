import sys
k = 15

def sort(data):
    for j in range(1, len(data)):
         key = data[j]
         i = j - 1
         while i >= 0 and data[i] > key:
             data[i + 1] = data[i]
             i -= 1
         data[i + 1] = key

    return data

def merge (left, right):
    l = 0
    r = 0
    res = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    while l < len(left):
        res.append(left[l])
        l += 1

    while r < len(right):
        res.append(right[r])
        r += 1

    return res

def merge_sort(data):
    if len(data) >= k:
        data = merge(merge_sort(data[0 : int(len(data) / 2)]), merge_sort(data[int(len(data) / 2) : len(data)]))
    else:
        data = sort(data)

    return data

data = sys.stdin.readline().split(' ')
for i in range(len(data)):
    data[i] = int(data[i])

data = merge_sort(data)
print(data)
