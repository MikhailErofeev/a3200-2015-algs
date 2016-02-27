from sys import stdin

def insert_sort(l, r):
    global numbers
    r += 1
    for i in range(l, r):
        cur_min = numbers[i]
        cur_id = i
        for j in range(i + 1, r):
            if (cur_min > numbers[j]):
                cur_min = numbers[j]
                cur_id = j
        numbers[i], numbers[cur_id] = numbers[cur_id], numbers[i]

def merge(l1, r1, l2, r2):
    global numbers
    lst = [int(0) for i in range(0, r1 - l1 + r2 - l2 + 2)]
    id_first = l1
    id_second = l2
    id = int(0)
    while (id_first <= r1) or (id_second <= r2):
        if (id_first > r1):
            lst[id] = numbers[id_second]
            id_second += 1
            id += 1
        elif (id_second > r2):
            lst[id] = numbers[id_first]
            id_first += 1
            id += 1
        elif (numbers[id_first] < numbers[id_second]):
            lst[id] = numbers[id_first]
            id += 1
            id_first += 1
        else:
            lst[id] = numbers[id_second]
            id_second += 1
            id += 1
    id = 0
    for i in range(l1, r1 + 1):
        numbers[i] = lst[id]
        id += 1
    for i in range(l2, r2 + 1):
        numbers[i] = lst[id]
        id += 1

def merge_sort(l, r):
    global numbers
    global k
    r += 1
    if (r - l <= k):
        insert_sort(l, r - 1)
    else:
        merge_sort(l, r - (r - l) / 2)
        merge_sort(r - (r - l) / 2 + 1, r - 1)
        merge(l, r - (r - l) / 2, r - (r - l) / 2 + 1, r - 1)

k = 11
numbers = [int(str) for str in stdin.readline().split()]
merge_sort(int(0), int(len(numbers)) - 1)
print numbers
