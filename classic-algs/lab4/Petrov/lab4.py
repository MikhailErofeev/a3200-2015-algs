from sys import stdin
a = list(map(int, stdin.readline().split()))
 
def insertion(a):
    for i in range(1, len(a)):
        c = a[i]
        j = i - 1
        while j >= 0 and a[j] > c:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = c
    return a
       
def merge(left, right):
    result = []
    left_i, right_i = 0, 0
    while len(left) > left_i  and len(right) > right_i:
        if  right[right_i] >= left[left_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1
    if left:
        result.extend(left[left_i:])
    if right:
        result.extend(right[right_i:])
    return result
 
def merge_sort(array):
    if len(array) <= 11:
        return insertion(array)
 
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
 
b = merge_sort(a)
for i in range(len(b)):
    print(b[i], end = ' ')
