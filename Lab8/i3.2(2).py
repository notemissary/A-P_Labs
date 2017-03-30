# Дыма Владимир. КНИТ16-А
# Алгоритм Бойера-Мура-Хорспула

import numpy as np

S = input('Введите строку: ')
W = input('Введите искомую строку: ')

T = np.arange(len(S)+len(W))
for i in range(0, len(S)+len(W)):
    T[i] = len(W)
for i in range(0, len(W)-1):
    T[ord(W[i])] = len(W) - 1 - i

skip = 0
while len(S) - skip >= len(W):
    i = len(W) - 1
    while S[skip + i] == W[i]:
        if i == 0:
            print(skip+1)
            exit()
        i -= 1
    skip += T[ord(S[skip + len(W) - 1])]
else:
    print('Nothing has been found.')
