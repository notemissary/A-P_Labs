# Дыма Владимир. КНИТ16-А
# Алгоритм Вагнера-Фишера

import numpy as np

S = input('Введите строку: ')
W = input('Введите подстроку: ')
m = len(S)
n = len(W)

d = np.ones((m+1, n+1), int)

# the distance of any first string to an empty second string
# (transforming the string of the first i characters of S into
# the empty string requires i deletions)
for i in range(1, m+1):
    d[i, 0] = i
for j in range(1, n+1):
    d[0, j] = j  # the distance of any second string to an empty first string

for j in range(1, n):
    for i in range(1, m):
        if S[i] == W[j]:
            d[i, j] = d[i-1, j-1]
        else:
            d[i, j] = min((d[i-1, j]+1,  # a deletion
                           d[i, j-1]+1,  # an insertion
                           d[i-1, j-1]+1))  # a substitution

print(d[m-1, n-1])
