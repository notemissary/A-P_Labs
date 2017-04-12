# Дыма Владимир. КНИТ16-А
# Bubble sort, selection sort, insertion sort

import random as r
import copy as c


def bubble(arr):
    for j in range(len(arr)-1, 0, -1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def selection(arr):
    for i in range(len(arr)):
        m = min(arr[i:])
        mi = arr[i:].index(m)
        arr[i+mi], arr[i] = arr[i], m
    return arr


def insertion(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
    return arr

N = int(input('Insert the length of the array: '))
A = r.sample([i for i in range(N**2)], N)
B = c.deepcopy(A)
C = c.deepcopy(A)

print(A)
print(bubble(A))
print(selection(B))
print(insertion(C))
