# Дыма Владимир. КНИТ16-А
# Bubble sort, selection sort, insertion sort,
# Cocktail shaker sort, Shellsort, Heapsort

from numpy import where, asarray, set_printoptions, empty, random, arange
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
    :return: Returns sorted array, comparision and swap amount.
    """
    c = 0
    s = 0
    h = 0
    for j in range(len(arr)-1, 0, -1):
        for i in range(len(arr)-1-h):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                s += 1
            c += 2
        c += 1
        h += 1
    return arr, c, s


def selection(arr):
    """
    Selection sort
    It is a sorting algorithm, specifically an in-place comparison sort.
    
    :param arr: Takes an array.
    :return: Returns sorted array, comparision number and swap amount.
    """
    s = 0
    c = 0
    for i in range(len(arr)):
        m = min(arr[i:])
        mi = where(arr[i:] == m)[0][0]
        arr[i+mi], arr[i] = arr[i], m
        s += 1
        c += 1
    return arr, c, s


def insertion(arr):
    """
    Insertion sort
    It is a sorting algorithm that builds the final sorted array one item 
    at a time.
    
    :param arr: Takes an array.
    :return: Returns sorted array, comparision number and swap amount.
    """
    c = 2
    s = 0
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
            c += 2
        else:
            if j != i - 1:
                s += 1
        arr[j+1] = x
        c += 1
    return arr, c, s


def shake(arr):
    """
    Cocktail shaker sort
    It is a variation of bubble sort that is both a stable sorting algorithm 
    and a comparison sort.

    :param arr: Takes an array.
    :return: Returns sorted array, comparision number and swap amount.
    """
    c = 1
    s = 0
    for i in range(len(arr)-1, 0, -1):
        c += 2
        swapped = False
        for j in range(i, 0, -1):
            c += 2
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                s += 1
                swapped = True
        if not swapped:
            return arr, c, s
        c += 1
        for j in range(i):
            c += 2
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                s += 1
                swapped = True
        if not swapped:
            return arr, c, s


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
    :return: Returns sorted array, comparision number and swap amount.
    """
    c = 2
    s = 0
    for gap in gaps:
        for i in range(gap, len(arr)):
            val = arr[i]
            j = i
            while j >= gap and arr[j-gap] > val:
                arr[j] = arr[j-gap]
                j -= gap
                c += 2
            else:
                if j != i:
                    s += 1
            arr[j] = val
            c += 1
        c += 1
    return arr, c, s


def heap(arr):
    """
    Heapsort
    It is a comparison-based sorting algorithm. 
    Heapsort can be thought of as an improved selection sort: like that 
    algorithm, it divides its input into a sorted and an unsorted region, 
    and it iteratively shrinks the unsorted region by extracting the largest 
    element and moving that to the sorted region.

    :param arr: Takes an array.
    :return: Returns sorted array, comparision and swap amount.
    """
    c = 3
    s = 0

    def siftdown(array, start, ending):
        nonlocal c, s
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
                s += 1
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
        s += 1
        end -= 1
        siftdown(arr, 0, end)
        c += 1
    return arr, c, s


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
    choice = input('Would you want to fill the array yourself? [y/n/idk]\n> '
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
                N = int(input('Input length of the array: '))
                if 0 < N <= lim:
                    print('Generating the array...', end=' ')
                    A = randarr(N)
                    if A is None:
                        print('Error! Not enough memory!')
                        continue
                    print('DONE!')
                    break
                elif N > lim:
                    print('Error! Array is too long for this machine.')
                else:
                    print('Error! Length MUST be positive number.')
            except ValueError:
                print('Error! Length must be integer!')
    elif choice == 'idk':
        print('LOL, you\'re indecisive. You need to choose something. '
              'Type \'exit\' to exit.')
        continue
    elif choice == 'exit':
        exit()
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
                   '0 - Get back\n'
                   '> ').lower()
        if ch == '1':
            print('=' * 75 + '\nOriginal array: \n{}'.format(A))
            t = time()
            res = bubble(A)
            t = time() - t
            print('Bubble sort sorted array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t) + '=' * 75)
        elif ch == '2':
            print('=' * 75 + '\nOriginal array: \n{}'.format(A))
            t = time()
            res = selection(A)
            t = time() - t
            print('Selection sort sorted array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t) + '=' * 75)
        elif ch == '3':
            print('=' * 75 + '\nOriginal array: \n{}'.format(A))
            t = time()
            res = insertion(A)
            t = time() - t
            print('Insertion sort sorted array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t) + '=' * 75)
        elif ch == '4':
            print('=' * 75 + '\nOriginal array: \n{}'.format(A))
            t = time()
            res = shake(A)
            t = time() - t
            print('Cocktail shaker sort sorted array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t) + '=' * 75)
        elif ch == '5':
            gp = shellprep(len(A))
            print('=' * 75 + '\nOriginal array: \n{}'.format(A))
            t = time()
            res = shell(A, gp)
            t = time() - t
            print('Shellsort sorted array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t) + '=' * 75)
        elif ch == '6':
            print('=' * 75 + '\nOriginal array: \n{}'.format(A))
            t = time()
            res = heap(A)
            t = time() - t
            print('Heapsort sorted array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t) + '=' * 75)
        elif ch == '9':
            print('Woah! FIRE!!!')
            print('Initializing testing arrays...', end=' ')
            BCA = WCD = arange(N)
            WCA = BCD = arange(N - 1, -1, -1)
            print('DONE!\n\nOriginal arrays:\n'
                  'Random array: \n{}\n'
                  'Best case array: \n{}\n'
                  'Worst case array: \n{}\n\n'
                  ''.format(A, BCA, WCA))
            print('Collecting garbage...', end=' ')
            del res, gp
            collect()
            print('DONE!\n\nBubble sort')
            t = time()
            res = bubble(deepcopy(A))
            t = time() - t
            print('=' * 75)
            print('Random array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res
            collect()
            t = time()
            res = bubble(deepcopy(BCA))
            t = time() - t
            print('Best case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res
            collect()
            t = time()
            res = bubble(deepcopy(WCA))
            t = time() - t
            print('Worst case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
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
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res
            collect()
            t = time()
            res = selection(deepcopy(BCA))
            t = time() - t
            print('Best case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res
            collect()
            t = time()
            res = selection(deepcopy(WCA))
            t = time() - t
            print('Worst case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
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
            print('Random array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res
            collect()
            t = time()
            res = insertion(deepcopy(BCA))
            t = time() - t
            print('Best case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res
            collect()
            t = time()
            res = insertion(deepcopy(WCA))
            t = time() - t
            print('Worst case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
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
            print('Random array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res
            collect()
            t = time()
            res = shake(deepcopy(BCA))
            t = time() - t
            print('Best case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res
            collect()
            t = time()
            res = shake(deepcopy(WCA))
            t = time() - t
            print('Worst case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
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
            print('Random array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res, gp
            collect()
            gp = shellprep(len(BCA))
            t = time()
            res = shell(deepcopy(BCA), gp)
            t = time() - t
            print('Best case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res, gp
            collect()
            gp = shellprep(len(WCA))
            t = time()
            res = shell(deepcopy(WCA), gp)
            t = time() - t
            print('Worst case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
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
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res
            collect()
            t = time()
            res = heap(deepcopy(BCA))
            t = time() - t
            print('Best case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  '\n'.format(res[0], res[1], res[2], t))
            del res
            collect()
            t = time()
            res = heap(deepcopy(WCA))
            t = time() - t
            print('Worst case array: \n{}\n'
                  'Comparisions: {} | Swaps: {} | Time: {:.6f} seconds'
                  ''.format(res[0], res[1], res[2], t))
            print('=' * 75)

            print('Collecting garbage...', end=' ')
            del res, A, BCA, BCD, WCA, WCD, t
            collect()
            print('DONE!')
            pass
        elif ch == '0':
            break
        else:
            print('Error! Choose a number of the algorithm.')
            continue
        try:
            del A, res, t
            collect()
        except NameError:
            pass
        break
    while True:
        ch = input('\nWanna try something again, huh? [y/n]\n> ').lower()
        if ch == 'y':
            print('Let be so.')
            break
        elif ch == 'n':
            print('Okay, bye!')
            exit()
        else:
            print('Error! Try again.')
