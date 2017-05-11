# Дыма Владимир. КНИТ16-А
from sys import setrecursionlimit
setrecursionlimit(10000)


def Ar(n, m):
    if n == 0:
        return m + 1
    if n > 0 and m == 0:
        return Ar(n-1, 1)
    return Ar(n-1, Ar(n, m-1))


def Ai(n, m):
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
    n, m = int(input('n: ')), int(input('m: '))
    print(Ar(n, m))
    print(Ai(n, m))
