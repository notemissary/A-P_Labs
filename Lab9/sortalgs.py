# Дыма Владимир. КНИТ16-А
# Bubble sort, selection sort, insertion sort,
# Cocktail shaker sort, Shellsort, Heapsort

from numpy import where, asarray, set_printoptions, empty
from random import sample, randint
from time import clock


def bubble(arr):
    """
    Bubble sort
    It is a  sorting algorithm that repeatedly steps through the list to 
    be sorted, compares each pair of adjacent items and swaps them if 
    they are in the wrong order.
    
    :param arr: Takes an array.
    :return: Returns sorted array.
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
    
    :param arr: Takes an array.
    :return: Returns sorted array.
    """
    for i in range(len(arr)):
        m = min(arr[i:])
        mi = where(arr[i:] == m)[0][0]
        arr[i+mi], arr[i] = arr[i], m
    return arr


def insertion(arr):
    """
    Insertion sort
    It is a sorting algorithm that builds the final sorted array one item 
    at a time.
    
    :param arr: Takes an array.
    :return: Returns sorted array.
    """
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
    return arr


def shake(arr):
    """
    Cocktail shaker sort
    It is a variation of bubble sort that is both a stable sorting algorithm 
    and a comparison sort.

    :param arr: Takes an array.
    :return: Returns sorted array and comparision number.
    """
    c = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        for j in range(left, right):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                c += 1
            else:
                c += 1
        right -= 1

        for j in range(right, left, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                c += 1
            else:
                c += 1
        left += 1
        c += 1
    else:
        c += 1
    return arr, c


def shell(arr):
    """
    Shellsort
    It is an in-place comparison sort.

    :param arr: Takes an array.
    :return: Returns sorted array and comparision number.
    """
    c = 0
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            val, j = arr[i], i
            while j >= gap and arr[j - gap] > val:
                arr[j] = arr[j - gap]
                j -= gap
                c += 2
            else:
                c += 1
            arr[j] = val
        gap //= 2
        c += 1
    else:
        c += 1
    return arr, c


def heap(arr):
    """
    Heapsort
    It is a comparison-based sorting algorithm. 
    Heapsort can be thought of as an improved selection sort: like that 
    algorithm, it divides its input into a sorted and an unsorted region, 
    and it iteratively shrinks the unsorted region by extracting the largest 
    element and moving that to the sorted region.

    :param arr: Takes an array.
    :return: Returns sorted array and comparision number
    """
    c = 0

    def siftdown(array, start, ending):
        nonlocal c
        root = start
        while 2 * root + 1 <= ending:
            child = 2 * root + 1
            swap = root
            if array[swap] < array[child]:
                swap = child
                c += 1
            else:
                c += 1
            if child + 1 <= ending and array[swap] < array[child + 1]:
                swap = child + 1
                c += 2
            else:
                c += 1
            if swap == root:
                c += 1
                return array
            else:
                array[root], array[swap] = array[swap], array[root]
                root = swap
                c += 1
            c += 1
        else:
            c += 1

    def heapify(array, arraylen):
        nonlocal c
        start = (arraylen - 2) // 2
        while start >= 0:
            siftdown(array, start, arraylen - 1)
            start -= 1
            c += 1
        else:
            c += 1
        return array

    arrlen = len(arr)
    heapify(arr, arrlen)
    end = arrlen - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        end -= 1
        siftdown(arr, 0, end)
        c += 1
    else:
        c += 1
    return arr, c


def randarr(num):
    return asarray(sample(range(-2 * num, 2 * num), num))


set_printoptions(threshold=10)
while True:
    choice = input('Would you want to fill the array yourself? [y/n]\n> '
                   '').lower()
    if choice == 'y':
        while True:
            try:
                N = int(input('Input the length of the array: '))
                if 0 < N <= 30:
                    A = empty(N, int)
                    for v in range(N):
                        while True:
                            try:
                                A[v] = int(input('Input an integer for {} element: '
                                                 ''.format(v+1)))
                            except (ValueError, IndexError):
                                print('Error! Try again!')
                                continue
                            break
                else:
                    print('Wrong length! Try again.')
                    continue
            except ValueError:
                print('Length must be integer!')
                continue
            break
    elif choice == 'n':
        A = randarr(randint(99900, 100100))
    else:
        print('Error! Answer with y for yes and n for no')
        continue
    while True:
        ch = input('What sort would you want to use?\n> ').lower()
        if ch == 'bubble sort':
            print('Original array: \n{}'.format(A))
            print('Bubble sort: \n{}\n'
                  '====================================================='
                  ''.format(bubble(A)))
        elif ch == 'selection sort':
            print('Original array: \n{}'.format(A))
            print('Selection sort: \n{}\n'
                  '====================================================='
                  ''.format(selection(A)))
        elif ch == 'insertion sort':
            print('Original array: \n{}'.format(A))
            print('Insertion sort: \n{}\n'
                  '====================================================='
                  ''.format(insertion(A)))
        elif ch == 'cocktail shaker sort':
            print('Original array: \n{}'.format(A))
            t = clock()
            res = shake(A)
            t = clock() - t
            print('Cocktail shaker sort: \n{}\nComparision number: {}\n'
                  'Time: {:.6f} seconds\n'
                  '====================================================='
                  ''.format(res[0], res[1], t))
        elif ch == 'shellsort':
            print('Original array: \n{}'.format(A))
            t = clock()
            res = shell(A)
            t = clock() - t
            print('Shellsort: \n{}\nComparision number: {}\n'
                  'Time: {:.6f} seconds\n'
                  '====================================================='
                  ''.format(res[0], res[1], t))
        elif ch == 'heapsort':
            print('Original array: \n{}'.format(A))
            t = clock()
            res = heap(A)
            t = clock() - t
            print('Heapsort: \n{}\nComparision number: {}\n'
                  'Time: {:.6f} seconds\n'
                  '====================================================='
                  ''.format(res[0], res[1], t))
        else:
            print('There\'s no such algorithm! Try again!')
            continue
        break
    while True:
        ch = input('Wanna try something again, huh? [y/n]\n> ').lower()
        if ch == 'y':
            print('Let be so.')
            break
        elif ch == 'n':
            print('Okay, bye!')
            exit()
        else:
            print('Error! Try again.')
