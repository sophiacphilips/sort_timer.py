#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 03/01/2023
#This program is designed to run a bubble and sort function, time how long each takes to run using randomly generated
#numbers and plot the times on a graph.

import time
import random
import matplotlib.pyplot

def bubble_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp


def insertion_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value


def sort_timer(func):
    '''
    decorator function finds the amount of time it takes for bubble insertion and sort insertion to run
    '''
    def sort_wrapper(t):
        begin = time.perf_counter()
        func(t)
        end = time.perf_counter()
        return (end-begin)
    return sort_wrapper


def compare_sorts(bub_list1, ins_list1):
    ''' compares bubble and sort insertion functions and plots them to a graph'''
    x_val = []
    y_val_bub = []
    y_val_ins = []
    testing_vals=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000] #number range for random testing values
    for r in testing_vals:
        random_nums = [random.randint(1, 10000) for x in range(r)]
        copy = list(random_nums) 

        bub_list2 = bub_list1(random_nums)
        ins_list2 = ins_list1(copy)

        x_val.append(r)
        y_val_bub.append(bub_list2)
        y_val_ins.append(ins_list2)

compare_sorts(sort_timer(bubble_sort), sort_timer(insertion_sort))

from matplotlib import pyplot
pyplot.plot([1, 2, 3, 4, 10], [1, 4, 9, 16, 100], 'ro--', linewidth=2, label='series 1')
pyplot.plot([1, 2, 3, 4, 10], [1, 3, 7, 20, 150], 'go--', linewidth=2, label='series 2')
pyplot.xlabel("the x label")
pyplot.ylabel("the y label")
pyplot.legend(loc='upper left')
pyplot.show()