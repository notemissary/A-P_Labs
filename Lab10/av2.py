# Дыма Владимир. КНИТ16-А
from numpy import empty, ndarray


def summa_r(d):
    """
    Summs elements of an matrix in recursive way.
    
    :param d: A matrix. 
    :return: Returns sum.
    """
    if type(d) != ndarray:
        return d
    elif len(d) == 0:
        return 0
    else:
        return summa_r(d[0]) + summa_r(d[1:])


def summa_i(d):
    """
    Summs elements of an matrix in iterative way.

    :param d: A matrix. 
    :return: Returns sum.
    """
    res = 0
    for i in d:
        for j in i:
            res += j
    return res


def mult_r(d):
    """
    Multiplicates elements of an matrix in recursive way.
    
    :param d: A matrix.
    :return: Returns sum.
    """
    if type(d) != ndarray:
        return d
    elif len(d) == 0:
        return 1
    else:
        return mult_r(d[0]) * mult_r(d[1:])


def mult_i(d):
    """
    Multiplicates elements of an matrix in iterative way.

    :param d: A matrix.
    :return: Returns sum.
    """
    res = 1
    for i in d:
        for j in i:
            res *= j
    return res


def search_r(d, e, s, g=0):
    """
    Searches for an element in a given matrix in recursive way.
    
    :param d: A matrix.
    :param e: An element to find.
    :param s: matrix shape.
    :param g: Counter.
    :return: Pair of coordinates.
    """
    def rows(d):
        """
        Parsing rows.
        
        :param d: A matrix.
        :return: Slice of the matrix if length is not 0 and 0 otherwise
        """
        if len(d) != 0:
            if cols(d[0]):
                return None
            return rows(d[1:])
        else:
            return 0

    def cols(d):
        """
        Parsing columns.
        
        :param d: A matrix.
        :return: Returns True of False.
        """
        nonlocal e, g
        if len(d) == 0:
            return False
        elif d[0] == e:
            return True
        else:
            g += 1
            return cols(d[1:])
    rows(d)
    return g//s, g%s


def search_i(N, e):
    """
    Finds an element in a matrix in iterative way
    
    :param N: Matrix
    :param e: An element to find.
    :return: Returns coordinates.
    """
    for i in range(len(N)):
        for j in range(len(N[i])):
            if N[i][j] == e:
                return i, j

while True:
    shape = int(input('Input matrix shape: '))
    N = empty((shape, shape), int)
    for i in range(len(N)):
        for j in range(len(N[i])):
            N[i][j] = int(input('N{}{}: '.format(i + 1, j + 1)))
    b = input('1 - Sum\n'
              '2 - Mult\n'
              '3 - Search\n'
              '> ')
    if b == '1':
        print(summa_r(N))
        print(summa_i(N))
    elif b == '2':
        print(mult_r(N))
        print(mult_i(N))
    else:
        e = int(input('e: '))
        print(search_r(N, e, shape))
        print(search_i(N, e))
