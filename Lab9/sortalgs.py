# Дыма Владимир. КНИТ16-А
# Bubble sort, selection sort, insertion sort,
# Cocktail shaker sort, Shellsort, Heapsort

from numpy import where, asarray, set_printoptions, empty, random
from time import time
from copy import deepcopy
from gc import collect, enable

print('Enabling garbage collector...', end=' ')
enable()
print('DONE!\nInitializing functions...', end=' ')


def bubble(arr):
    """
    Bubble sort
    It is a  sorting algorithm that repeatedly steps through the list to 
    be sorted, compares each pair of adjacent items and swaps them if 
    they are in the wrong order.
    
    :param arr: Takes an array.
    :return: Returns sorted array, comparision and switch number.
    """
    c = 0
    e = 0
    h = 0
    for j in range(len(arr)-1, 0, -1):
        for i in range(len(arr)-1-h):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                e += 1
            c += 2
        c += 1
        h += 1
    return arr, c, e


def selection(arr):
    """
    Selection sort
    It is a sorting algorithm, specifically an in-place comparison sort.
    
    :param arr: Takes an array.
    :return: Returns sorted array, comparsision number and switches number
    """
    e = 0
    c = 0
    for i in range(len(arr)):
        m = min(arr[i:])
        mi = where(arr[i:] == m)[0][0]
        arr[i+mi], arr[i] = arr[i], m
        e += 1
        c += 1
    return arr, c, e


def insertion(arr):
    """
    Insertion sort
    It is a sorting algorithm that builds the final sorted array one item 
    at a time.
    
    :param arr: Takes an array.
    :return: Returns sorted array, comparision number and switch number.
    """
    c = 2
    e = 0
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
            c += 2
        arr[j+1] = x
        e += 1
        c += 1
    return arr, c, e


def shake(arr):
    """
    Cocktail shaker sort
    It is a variation of bubble sort that is both a stable sorting algorithm 
    and a comparison sort.

    :param arr: Takes an array.
    :return: Returns sorted array, comparision number and switch number.
    """
    c = 1
    e = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        for j in range(left, right):
            c += 2
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                e += 1
        right -= 1

        for j in range(right, left, -1):
            c += 2
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                e += 1
        left += 1

        c += 1
    return arr, c, e


def shellprep(lenarr):
    if lenarr > 4000:
        # Robert Sedgewick's gap sequence (1986)
        # Formulas:
        # a(n) = 9*2^n - 9*2^(n/2) + 1 if n is even;
        # a(n) = 8*2^n - 6*2^((n+1)/2) + 1 if n is odd.
        # G.f.: (8*x^4 + 2*x^3 - 8*x^2 - 4*x - 1)/((x-1)*(2*x+1)*(2*x-1)*(2*x^2-1))
        g = asarray((4294770689, 2415771649, 1073643521, 603906049, 268386305,
                     150958081, 67084289, 37730305, 16764929, 9427969,
                     4188161, 2354689, 1045505, 587521, 260609, 146305,
                     64769, 36289, 16001, 8929, 3905, 2161, 929, 505, 209,
                     109, 41, 19, 5, 1))
    else:
        # Marcin Ciura's gap sequence (2001)
        # Experimentaly derived. Best for less than 4000 elements arrays
        g = asarray((1750, 701, 301, 132, 57, 23, 10, 4, 1))
    w = 0
    for gg in g:
        if lenarr >= gg:
            w = where(g == gg)[0][0]
            break
    return g[w:]


def shell(arr, gaps):
    """
    Shellsort
    It is an in-place comparison sort.
    It uses Sedgewick's sequence if array length is more than 4000 elements.
    Uses Ciura's sequence if array length is less than or is 4000 elements.
    Both sequences are the best-known for such lengths.

    :param arr: Takes an array.
    :param gaps: Takes a gaps sequence.
    :return: Returns sorted array, comparision number and switch number.
    """
    c = 2
    e = 0
    for gap in gaps:
        for i in range(gap, len(arr)):
            val = arr[i]
            j = i
            while j >= gap and arr[j-gap] > val:
                arr[j] = arr[j-gap]
                j -= gap
                c += 2
            arr[j] = val
            e += 1
            c += 1
        c += 1
    return arr, c, e


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
    c = 3
    e = 0

    def siftdown(array, start, ending):
        nonlocal c, e
        root = start
        child = (root << 1) + 1
        while child <= ending:
            c += 4
            swap = root
            if array[swap] < array[child]:
                swap = child
            if child + 1 <= ending and array[swap] < array[child + 1]:
                swap = child + 1
            if swap == root:
                return array
            else:
                array[root], array[swap] = array[swap], array[root]
                e += 1
                root = swap
            child = (root << 1) + 1

    def heapify(array, arraylen):
        nonlocal c
        start = (arraylen - 2) >> 1
        while start >= 0:
            siftdown(array, start, arraylen - 1)
            start -= 1
            c += 1
        return array

    arrlen = len(arr)
    heapify(arr, arrlen)
    end = arrlen - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        e += 1
        end -= 1
        siftdown(arr, 0, end)
        c += 1
    return arr, c, e


def randarr(num):
    try:
        return random.permutation(num)
    except (MemoryError, OverflowError):
        return None

print('DONE!\nReserving variables...', end=' ')
res, gp = None, None
print('DONE!\nSetting up print options...', end=' ')
set_printoptions(threshold=10, edgeitems=4)

print('DONE!\n\n\nWelcome to SortAlgs!')
while True:
    choice = input('Would you want to fill the array yourself? [y/n]\n> '
                   '').lower()
    if choice == 'y':
        lim = 30
        while True:
            try:
                N = int(input('Input the length of the array: '))
                if 0 < N <= lim:
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
                    print('Wrong length! Set it between 0 and 30!')
                    continue
            except ValueError:
                print('Length must be integer!')
                continue
            break
    elif choice == 'n':
        lim = 50000000
        while True:
            try:
                integer = int(input('Input length of the array: '))
                if 0 < integer <= lim:
                    print('Generating the array...', end=' ')
                    A = randarr(integer)
                    if A is None:
                        print('Error! Not enough memory!')
                        continue
                    print('DONE!')
                    break
                elif integer > lim:
                    print('Error! Array is too long for this machine.')
                else:
                    print('Error! Length MUST be positive number.')
            except ValueError:
                print('Error! Length must be integer!')
    else:
        print('Error! Answer with y for yes and n for no')
        continue
    while True:
        ch = input('What sorting algorithm would you want to use?\n'
                   '1 - Bubble sort\n'
                   '2 - Selsection sort\n'
                   '3 - Insertion sort\n'
                   '4 - Cocktail shaker sort\n'
                   '5 - Shellsort\n'
                   '6 - Heapsort\n'
                   '9 - TEST \'EM ALL!\n'
                   '> ').lower()
        if ch == '1':
            print('Original array: \n{}'.format(A))
            t = time()
            res = bubble(A)
            t = time() - t
            print('Bubble sort: \nArray: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds'
                  '====================================================='
                  ''.format(res[0], res[1], res[2], t))
        elif ch == '2':
            print('Original array: \n{}'.format(A))
            t = time()
            res = selection(A)
            t = time() - t
            print('Selection sort: \nArray: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds'
                  '====================================================='
                  ''.format(res[0], res[1], res[2], t))
        elif ch == '3':
            print('Original array: \n{}'.format(A))
            t = time()
            res = insertion(A)
            t = time() - t
            print('Insertion sort: \nArray: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds'
                  '====================================================='
                  ''.format(res[0], res[1], res[2], t))
        elif ch == '4':
            print('Original array: \n{}'.format(A))
            t = time()
            res = shake(A)
            t = time() - t
            print('Cocktail shaker sort: \nArray: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds\n'
                  '====================================================='
                  ''.format(res[0], res[1], res[2], t))
        elif ch == '5':
            gp = shellprep(len(A))
            print('Original array: \n{}'.format(A))
            t = time()
            res = shell(A, gp)
            t = time() - t
            print('Shellsort: \nArray: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds\n'
                  '====================================================='
                  ''.format(res[0], res[1], res[2], t))
        elif ch == '6':
            print('Original array: \n{}'.format(A))
            t = time()
            res = heap(A)
            t = time() - t
            print('Heapsort: \nArray: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds\n'
                  '====================================================='
                  ''.format(res[0], res[1], res[2], t))
        elif ch == '9':
            print('Original array: \n{}'.format(A))
            print('Woah! FIRE!!!')
            print('Collecting garbage...', end=' ')
            del res, gp
            collect()
            print('DONE!\n\nBubble sort')
            t = time()
            res = bubble(deepcopy(A))
            t = time() - t
            print('=' * 75)
            print('Array: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds'
                  ''.format(res[0], res[1], res[2], t))
            print('=' * 75)

            print('Collecting garbage...', end=' ')
            del res
            collect()
            print('DONE!\n\nSelection sort')
            t = time()
            res = selection(deepcopy(A))
            t = time() - t
            print('=' * 75)
            print('Array: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds'
                  ''.format(res[0], res[1], res[2], t))
            print('=' * 75)

            print('Collecting garbage...', end=' ')
            del res
            collect()
            print('DONE!\n\nInsertion sort')
            t = time()
            res = insertion(deepcopy(A))
            t = time() - t
            print('=' * 75)
            print('Array: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds'
                  ''.format(res[0], res[1], res[2], t))
            print('=' * 75)

            print('Collecting garbage...', end=' ')
            del res
            collect()
            print('DONE!\n\nCocktail shaker sort')
            t = time()
            res = shake(deepcopy(A))
            t = time() - t
            print('=' * 75)
            print('Array: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds'
                  ''.format(res[0], res[1], res[2], t))
            print('=' * 75)

            print('Collecting garbage...', end=' ')
            del res
            collect()
            print('DONE!\n\nShellsort')
            gp = shellprep(len(A))
            t = time()
            res = shell(deepcopy(A), gp)
            t = time() - t
            print('=' * 75)
            print('Array: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds'
                  ''.format(res[0], res[1], res[2], t))
            print('=' * 75)

            print('Collecting garbage...', end=' ')
            del res, gp
            collect()
            print('DONE!\n\nHeapsort')
            t = time()
            res = heap(deepcopy(A))
            t = time() - t
            print('=' * 75)
            print('Array: \n{}\n'
                  'Comparisions: {} | Exchanges: {}\n'
                  'Time: {:.6f} seconds'
                  ''.format(res[0], res[1], res[2], t))
            print('=' * 75)

            print('Collecting garbage...', end=' ')
            del res
            collect()
            print('DONE!')
            pass
        else:
            print('Error! Choose a number of the algorithm.')
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
