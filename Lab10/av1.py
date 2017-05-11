# Дыма Владимир. КНИТ16-А
def Nod_i(n, m):
    """
    Finds greatest common divisor in iterative way.
    
    :param n: The first number.
    :param m: The second number.
    :return: The greatest common divisor.
    """
    while m != 0 and n != 0:
        if n > m:
            n %= m
        else:
            m %= n
    return n + m


def nod_r(n, m):
    """
    Finds greatest common divisor in recursive way.
    
    :param n: The first number.
    :param m: The second number.
    :return: The greatest common divisor. 
    """
    if m == 0:
        return n
    else:
        return nod_r(m, n % m)

while True:
    try:
        n, m = int(input('Input n: ')), int(input('Input m: '))
    except ValueError:
        print('Error! Input an integer.')
        continue
    print(nod_r(n, m))
    print(Nod_i(n, m))

