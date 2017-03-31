# Дыма Владимир. КНИТ16-А
# Алгоритм Вагнера-Фишера

import numpy as np

S = (input('Введите строку: ').lower()).split(', ')
W = input('Введите подстроку: ').lower()
n = len(W)

for k in S:
    m = len(k)
    d = np.ones((m + 1, n + 1), int)

    # the distance of any first string to an empty second string
    # (transforming the string of the first i characters of S into
    # the empty string requires i deletions)
    for i in range(0, m):
        d[i, 0] = i
    for j in range(0, n):
        d[0, j] = j  # the distance of any second string to an empty first string
    for j in range(1, n):
        for i in range(1, m):
            if k[i] == W[j]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min((d[i-1, j]+1,  # a deletion
                               d[i, j-1]+1,  # an insertion
                               d[i-1, j-1]+1))  # a substitution

    p = d[m, n]
    if p <= m % 3:
        print(k, end=', ')
