# Дыма Владимир. КНИТ16-А
from sys import setrecursionlimit, getrecursionlimit
i = 1001
print('Setting the maximum recursion limit...')
while True:
    try:
        setrecursionlimit(i)
        i += 100
    except OverflowError:
        setrecursionlimit(i-100)
        break
print('Recursion limit set to {}'.format(getrecursionlimit()))
lvl = None


def Ar(m, n, level=0):
    """
    Recursive Ackermann function.
    
    :param m: The first element.
    :param n: The second element.
    :return: Number.
    """
    global lvl
    lvl = level
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return Ar(m-1, 1, level=lvl+1)
    return Ar(m-1, Ar(m, n-1, level=lvl+1), level=lvl+1)


def Ai(m, n):
    """
    Iterative Ackermann function.
    
    :param m: The first element.
    :param n: The second element.
    :return: Number.
    """
    stack = []
    while True:
        if not m:
            if not stack:
                return n + 1
            m, n = stack.pop(), n + 1
        elif not n:
            m, n = m - 1, 1
        else:
            stack.append(m - 1)
            n -= 1


while True:
    try:
        n, m = int(input('Input n: ')), int(input('Input m[less than 5]: '))
        if n >= 2 and m >= 4:
            print('Stuck would overflow! Input the other numbers.')
            continue
        # print('Result of iterations: {}'.format(Ai(m, n)))
        print('Result of recrustion: {}. Recursion depth: {}'
              ''.format(Ar(m, n), lvl))
    except ValueError:
        print('ERR204: Try again!')
