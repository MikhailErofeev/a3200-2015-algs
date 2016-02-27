__author__ = "Dmitry Petrushin"

from random import randint as rand
from time import time

import matplotlib as mpl
import pylab as plt
import brewer2mpl

from merge_sort import extendedmergesort as merge_sort
from quick_sort import quicksort as quick_sort
from radix_sort import extended_radix_sort as radix_sort


def different(size):
    return [rand(-1000000, 1000000) for _ in range(size)]


def positive(size):
    return [rand(0, 10000) for _ in range(size)]


def partially_sorted(size):
    arr = [0 for _ in range(size)]
    arr[0] = rand(0, 10000)
    for i in range(1, size):
        if rand(0, 100) < 5:
            arr[i] = arr[i - 1]
        else:
            arr[i] = (arr[i - 1] + rand(0, 10000)) % 10000
    return arr


def ascending_sorted(size):
    return sorted([rand(0, 10000) for _ in range(size)])


def descending_sorted(size):
    return sorted([rand(0, 10000) for _ in range(size)])[::-1]


def same(size):
    num = rand(-1000000, 1000000)
    return [num for _ in range(size)]


types = {"Numbers in [-1.000.000, 1.000.000]": different,
         "Numbers in [0, 10.000]": positive,
         "Partially sorted numbers in [0, 10.000]": partially_sorted,
         "Ascending sorted numbers in  [0, 10.000]": ascending_sorted,
         "Descending sorted numbers in  [0, 10.000]": descending_sorted,
         "Same numbers in [-1.000.000, 1.000.000]": same
}

functions = {"Merge sort": merge_sort,
             "Quick sort": quick_sort,
             "Radix sort": radix_sort,
             "Built-in sort": sorted}


def count(typ, func):
    element_count = 100
    mls = []
    cnt = []
    while element_count < 1000200:
        millis = 0.0
        for _ in range(5):
            arr = typ(element_count)
            t1 = time()
            func(arr)
            t2 = time()
            millis += t2 - t1
        millis /= 5.0
        mls.append(millis)
        cnt.append(element_count)
        element_count += 100000
    return mls, cnt


def compare_sorts():
    # Color adjustment
    mpl.rcParams['axes.color_cycle'] = brewer2mpl.get_map('Set2', 'qualitative', 5).mpl_colors
    fig = plt.figure(1)
    fig.set_facecolor('#DADFE1')
    fig.set_edgecolor('none')
    #
    current_frame = 1
    for type_def, typ in types.items():
        # Design adjustment
        plt.subplot(2, 3, current_frame)
        plt.xlabel("Size, element", fontsize=14, color='#0B2C3C')
        plt.ylabel("Time, sec", fontsize=14, color='#0B2C3C')
        plt.rc('axes', grid=True, facecolor=[0.85, 0.87, 0.88, 0.5], edgecolor='none')
        #
        print("Passing: ", type_def)
        for func_name, func in functions.items():
            print("\tUsing ", func_name)
            millis, sizes = count(typ, func)
            plt.plot(sizes, millis, label=func_name)
        plt.title(type_def, fontsize=18, color='#FF6666')
        plt.legend(loc="upper left", title="Sorts")
        current_frame += 1
    plt.tight_layout()
    plt.show()


compare_sorts()



