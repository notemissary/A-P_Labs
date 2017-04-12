# Дыма Владимир. КНИТ16-А
# Cocktail shaker sort, Shellsort, Heapsort

import random as r
import copy as c


def shake(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        for j in range(left, right):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        right -= 1

        for j in range(right, left, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
        left += 1
    return arr


def shell(arr):
    return arr


def heap(arr):
    return arr

N = int(input('Insert the length of the array: '))
A = r.sample([i for i in range(N**2)], N)
B = c.deepcopy(A)
C = c.deepcopy(A)

print(A)
print(shake(A))
print(shell(B))
print(heap(C))