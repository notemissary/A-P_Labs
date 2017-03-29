# Дыма Владимир. КНИТ16-А
# Алгоритм Вагнера-Фишера

import numpy as np

S = input('Введите строку: ')
W = input('Введите подстроку: ')
m = len(S)
n = len(W)

d = np.zeros((m, n), int)
for i in range(0, m):
    d[i, 0] = i
for j in range(0, n):
    d[0, j] = j

for j in range(1, n):
    for i in range(1, m):
        if S[i] == W[j]:
            d[i, j] = d[i-1, j-1]
        else:
            d[i, j] = min((d[i-1, j]+1,
                           d[i, j-1]+1,
                           d[i-1, j-1]+1))
print(d[m-1, n-1])
