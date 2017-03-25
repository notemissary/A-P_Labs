# Дыма Владимир. КНИТ16-А
# Алгоритм Кнута-Морриса-Пратта

import numpy as np

S = input('Введите строку: ')
W = input('Введите искомую подстроку: ')
T = np.arange(0, len(S)+1)
pos = 2
cnd = 0
T[0] = -1
T[1] = 0
while pos < len(W):
    if W[pos-1] == W[cnd]:
        T[pos] = cnd+1
        cnd += 1
        pos += 1
    elif cnd > 0:
        cnd = T[cnd]
    else:
        T[pos] = 0
        pos += 1

i = m = 0
while m+i < len(S):
    if W[i] == S[m+i]:
        if i == len(W)-1:
            print('Успех! Подстрока найдена на позиции {}.'.format(m))
            break
        i += 1
    else:
        if T[i] > -1:
            m += i - T[i]
            i = T[i]
        else:
            m += 1
            i = 0
else:
    print('Провал! Подстрока не найдена.')
