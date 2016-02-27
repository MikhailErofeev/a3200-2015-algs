__author__ = "Dmitry Petrushin"


def merge(li1, li2):
    a = 0
    b = 0
    length = len(li1) + len(li2)
    res = [0 for i in range(0, length)]
    for i in range(0, length):
        if b < len(li2) and a < len(li1):
            if li1[a] > li2[b]:
                res[i] = li2[b]
                b += 1
            else:
                res[i] = li1[a]
                a += 1
        elif b < len(li2):
            res[i] = li2[b]
            b += 1
        else:
            res[i] = li1[a]
            a += 1
    return res


def insertionsort(li):
    for i in range(1, len(li)):
        j = i
        while j > 0 and li[j - 1] > li[j]:
            li[j - 1], li[j] = li[j], li[j - 1]
            j -= 1
    return li


def extendedmergesort(li):
    if len(li) < 100:
        return insertionsort(li)
    else:
        return merge(extendedmergesort(li[0:len(li) // 2]), extendedmergesort(li[len(li) // 2 + 1:len(li)]))

