from numpy import empty, ndarray, reshape


def summa_r(d):
    if type(d) != ndarray:
        return d
    elif len(d) == 0:
        return 0
    else:
        return summa_r(d[0]) + summa_r(d[1:])


def summa_i(d):
    res = 0
    for i in d:
        for j in i:
            res += j
    return res



def mult_r(d):
    if type(d) != ndarray:
        return d
    elif len(d) == 0:
        return 1
    else:
        return mult_r(d[0]) * mult_r(d[1:])


def mult_i(d):
    res = 1
    for i in d:
        for j in i:
            res *= j
    return res

g = 0
flag = True


def search_r(d, e, s, g):
    def rows(d):
        if len(d) != 0:
            if cols(d[0]):
                return None
            return rows(d[1:])
        else:
            return 0

    def cols(d):
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
    # d = d.reshape(-1)
    # if d[0] == e:
    #     return g//s, g%s
    # else:
    #     g += 1
    #     return search_r(d[1:], e, s, g)




def search_i(N, e):
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
        # res = search_r(N, e)
        # print(res)
        # print((res//shape, res%shape))
        print(search_r(N, e, shape, g))
        print(search_i(N, e))
