# Дыма Владимир. КНИТ16-А
def Nod_i(n, m):
    while m != 0 and n != 0:
        if n > m:
            n %= m
        else:
            m %= n
    return n + m


def nod_r(n, m):
    if m == 0:
        return n
    else:
        return nod_r(m, n % m)

while True:
    n, m = int(input('n: ')), int(input('m: '))
    print(nod_r(n, m))
    print(Nod_i(n, m))

