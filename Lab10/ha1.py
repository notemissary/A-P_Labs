# Дыма Владимир. КНИТ16-А
from sys import setrecursionlimit
setrecursionlimit(10000)


def Ar(n, m):
    """
    Recursive Ackermann function.
    
    :param n: The first element.
    :param m: The second element.
    :return: Number.
    """
    if n == 0:
        return m + 1
    if n > 0 and m == 0:
        return Ar(n-1, 1)
    return Ar(n-1, Ar(n, m-1))


def Ai(n, m):
    """
    Iterative Ackermann function.
    
    :param n: The first element.
    :param m: The second element.
    :return: Number.
    """
    stack = []
    while True:
        if not n:
            if not stack:
                return m + 1
            n, m = stack.pop(), m + 1
        elif not m:
            n, m = n - 1, 1
        else:
            stack.append(n - 1)
            m -= 1


while True:
    n, m = int(input('Input n[less than 5]: ')), int(input('m: '))
    if n >= 4 and m >1:
        print('Stuck would overflow! Input the other numbers.')
        continue
    print(Ar(n, m))
    print(Ai(n, m))
