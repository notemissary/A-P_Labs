# Дыма Владимир. КНИТ16-А
def func(n):
    a = [1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22, 27, 32, 38, 46, 54,
         64, 76, 89, 104, 122, 142, 165, 192, 222, 256, 296, 340, 390, 448,
         512, 585, 668, 760, 864, 982, 1113, 1260, 1426, 1610, 1816, 2048,
         2304, 2590, 2910, 3264, 3658, 4097, 4582, 5120, 5718, 6378]
    return a[n]


def func_r(n):
    """
    Counts number of possible distinct partitions of a given number.

    :param n: A number.
    :return: Returns amount of possible distinct partitions.
    """
    def p(n, k):
        """
        Minor counter.

        :param n: Number.
        :param k: Iteration number.
        :return: Sum.
        """
        if n == 0 and k == 0:
            return 1
        if n <= 0 or k <= 0:
            return 0
        return p(n-k, k) + p(n-1, k-1)
    res = []
    if n == 0 or n == 1:
        return 0
    for i in range(1, n):
        res.append(p(n, i))
    return max(res)


while True:
    n = int(input('Input n: '))
    print('Number of distinct parts: {}'.format(func_r(n)))
    print(func(n))
