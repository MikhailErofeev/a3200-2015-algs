__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

from sys import stdin as inp
from sys import stdout as out


class MaxHistogram:
    def __init__(self, array):
        self.array = array
        self.result = 0
        self.area = 0
        self.current = -1

    def __counting(self, i):
        if self.array[i] >= self.current:
            self.result = max(self.result, self.area)
            self.area = 0
            self.current = self.array[i]
        else:
            self.area += self.current - self.array[i]

    def max_histograms_area(self):
        for i in range(len(self.array)):
            self.__counting(i)
        self.area = 0
        self.current = -1
        for i in range(len(self.array))[::-1]:
            self.__counting(i)
        return self.result


if __name__ == '__main__':
    hist = MaxHistogram([int(i) for i in inp.readline().split()])
    out.write(str(hist.max_histograms_area()))
