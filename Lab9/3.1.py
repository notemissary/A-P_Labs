# Дыма Владимир. КНИТ16-А
# Bubble sort, selection sort, insertion sort

import random as r
import copy as c


def bubble(arr):
    """
    Bubble sort
    It is a  sorting algorithm that repeatedly steps through the list to 
    be sorted, compares each pair of adjacent items and swaps them if 
    they are in the wrong order.
    
    :param arr: 
    :return:
    """
    for j in range(len(arr)-1, 0, -1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def selection(arr):
    """
    Selection sort
    It is a sorting algorithm, specifically an in-place comparison sort.
    
    :param arr: 
    :return:
    """
    for i in range(len(arr)):
        m = min(arr[i:])
        mi = arr[i:].index(m)
        arr[i+mi], arr[i] = arr[i], m
    return arr


def insertion(arr):
    """
    Insertion sort
    It is a sorting algorithm that builds the final sorted array one item 
    at a time.
    
    :param arr: 
    :return:
    """
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
    return arr

N = int(input('Insert the length of the array: '))
A = r.sample(range(-2 * N, 2 * N), N)
B = c.deepcopy(A)
C = c.deepcopy(A)

print('Original array: \n{}'.format(A))
print('Cocktail bubble sort: \n{}'.format(bubble(A)))
print('Selection sort: \n{}'.format(selection(B)))
print('Insertion sort: \n{}'.format(insertion(C)))
