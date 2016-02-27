__author__ = 'Nikita Rybkin'
from time import time
import pylab
from mergesort import merge_sort
from radixsort import radix_sort
from quicksort import quick_sort

from random import randint


def generate_random_array(lo, hi, size):
    ans = [randint(lo, hi) for i in range(size)]
    for i in range(1, size):
        if randint(0, 1000000) < 30000:
            ans[randint(0, i)] = ans[i - 1]
    return ans


def positive_and_negative(size):
    return generate_random_array(-1000000, 1000000, size)


def positive(size):
    return generate_random_array(0, 10000, size)


def partially_sorted(size):
    hi = 10000
    ans = [0 for i in range(size)]
    ans[0] = randint(0, hi)
    for i in range(1, size):
        if randint(0, 1000000) < 30000:
            ans[i] = ans[i - 1]
        else:
            ans[i] = (ans[i - 1] + randint(0, hi)) % hi
    return ans


def ascending_sorted(size):
    ans = [0 for i in range(size)]
    ans[0] = randint(0, 10000)
    for i in range(1, size):
        if randint(0, 1000000) < 30000:
            ans[i] = ans[i - 1]
        else:
            ans[i] = ans[i - 1] + randint(0, (10000 - ans[i - 1]) // 10)
    return ans


def descending_sorted(size):
    ans = ascending_sorted(size)
    ans.reverse()
    return ans


def unique_number(size):
    num = randint(-1000000, 1000000)
    return [num for i in range(size)]


root = "/"
parts = __file__.split('/')
for i in range(1, len(parts) - 3):
    root += parts[i] + '/'


def grade(sort_func, array_generator, size):
    millis = 0.0
    for i in range(5):
        array = array_generator(size)
        t1 = time()
        sort_func(array)
        t2 = time()
        millis += t2 - t1
    millis /= 5.0
    return millis


sort_functions = {"Quick sort": quick_sort,
                  "Merge sort": merge_sort,
                  "Radix sort": radix_sort,
                  "Built-in sort": sorted}

generators = {"Array of random integers from [-1e6, 1e6]": positive_and_negative,
              "Array of random inegerts from [0, 1e4]": positive,
              "Array with some sorted subarrays": partially_sorted,
              "Already sorted array": ascending_sorted,
              "Descending sorted array": descending_sorted,
              "Array with the only distinct element": unique_number}

if __name__ == "__main__":

    sizes = [100 + 100000 * i for i in range(6)]
    crnt = 1

    for gen_name, gen in generators.items():
        pylab.subplot(2, 3, crnt)
        pylab.xlabel("size, elements")
        pylab.ylabel("time, sec")
        print("Now passing: %s" % gen_name)
        for func_name, func in sort_functions.items():
            millis = []
            for size in sizes:
                millis.append(grade(func, gen, size))
                print("\tUsing %s on array of size %s" % (func_name, size))
            print("\t***\n\n")
            pylab.plot(sizes, millis, label=func_name)
        pylab.title(gen_name)
        pylab.legend(loc='upper left', title="Sorts")
        crnt += 1

    pylab.show()