import random
from sys import stdin
 
class Heap:
    def __init__(self):
        self.a = []
    def _down(self, i):
        while 2 * i + 1 < len(self.a):
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < len(self.a) and self.a[right] < self.a[left]:
                j = right
            if self.a[i] <= self.a[j]:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j
    def _up(self, i):
        while i > 0 and self.a[i] < self.a[(i - 1) // 2]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2
    def min(self):
        res = self.a[0]
        if (len(self.a) > 1):
            self.a[0] = self.a.pop()
        else:
            self.a.pop()
        self._down(0)
        return res
    def insert(self, k):
        self.a.append(k)
        self._up(len(self.a) - 1)
 
def part1(a, k):
    h = Heap()
    for i in a:
        h.insert(i)
        if (len(h.a) > k):
            h.min()
    return h.a
 
 
def _partition5(a, l, r):
    for i in range(l, r):
        for j in range(i, r):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return (r + l) // 2
 
def _partition(a, l, r):
    if (r - l <= 4):
        return _partition5(a, l, r)
    t = []
    for i in range(5):
        randr = random.randint(l, r - 4)
        ta = a[randr:randr + 5]
        t.append(ta[_partition5(ta, 0, 4)])
    _partition5(t, 0, 4)
    x = t[2]
    i = l
    j = r
    while 1:
        while a[i] < x:
            i = i + 1
        while a[j] > x:
            j = j - 1
        if i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:
            return j
           
 
def part2(a, n):
    if len(a) == 1:
        return a[0]
    left = 0
    right = len(a) - 1
    k = len(a) - n - 1
    b = sorted(a)
    while 1:
        mid = _partition(a, left, right)
        if mid == k:
            return a[-n:]
        elif k < mid:
            right = mid
        else:
            left = mid + 1
 
if __name__ == '__main__':
    a = [int(i) for i in stdin.readline().split()]
    n = int(input())
    r1 = part1(a, n)
    print (r1)
    r2 = part2(a, n)
    print(r2)
