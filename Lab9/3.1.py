# Дыма Владимир. КНИТ16-А
# Bubble sort, selection sort, insertion sort

import random as r

def bubble(arr):
    k = 0
    while k < len(arr):
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
        k += 1
    return arr


def selection(arr):
    for i in range(len(arr)-1):
        m = min(arr[i+1:])
        if arr[i] > m:
            arr[i], arr[arr.index(m)] = \
                arr[arr.index(min(m))], arr[i]
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
A = B = C = r.sample([i for i in range(N**2)], N)

print(A)
print(bubble(A))
print(selection(B))
print(insertion(C))
