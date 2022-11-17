# Author: Faith Elledge
# Githubuser:
# Date: 11/16/22
# Description:
import numbers
import time
import random
from matplotlib import pyplot
from functools import wraps

def sort_timer(func):
    """ Times how many seconds it takes the decorated function to run"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        return end - start
    return wrapper

@sort_timer
def bubble_sort(num_list):
    """ Sorts List in asending Order"""
    for sort_num in range(len(num_list) - 1):
        for swap_num in range(len(num_list) - sort_num - 1):
            if num_list[swap_num] > num_list[swap_num + 1]:
                temp = num_list[swap_num]
                num_list[swap_num] = num_list[swap_num + 1]
                num_list[swap_num + 1] = temp

@sort_timer
def insertion_sort(num_list):
    """Builds the sorted list one element at a time by comparing each item with the rest
     of the list and inserting in into its correct position"""
    for i in range(1, len(num_list)):
        value = num_list[i]
        pos = i - 1
        while pos >= 0 and num_list[pos] > value:
            num_list[pos + 1] = num_list[pos]
            pos -= 1
            num_list[pos + 1] = value


def compare_sorts(dec_bubble1, dec_bubble2):
    """ Takes two decorated sort functions as parameters"""
    x_values = []
    y_values1 = []
    y_values2 = []

    for size in range(1000, 10001, 1000):
        x_values.append(size)
        num_list = []
        for x in range(size):
            num_list.append(random.randint(1, 10000))
    y_values1.append(dec_bubble1(numbers))
    y_values2.append(dec_bubble2(numbers))

    pyplot.plot(x_values, y_values1, 'ro--', linewidth=2, label="Bubble Sort")
    pyplot.plot(x_values, y_values2, 'ro--', linewidth=2, label="Insertation Sort")
    pyplot.xlabel("Size")
    pyplot.ylabel(" Time in seconds ")
    pyplot.legend(loc='upper left')
    pyplot.show()

compare_sorts(bubble_sort, insertion_sort)
