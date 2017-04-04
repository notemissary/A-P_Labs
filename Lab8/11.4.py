# Дыма Владимир. КНИТ16-А
# Вычислите определитель квадратной матрицы (массива)

import numpy as np
import random as r


def det(ma, mul=1):
    w = len(ma)
    if w == 1:
        return mul * ma[0][0]
    else:
        s = -1
        res = 0
        for i in range(w):
            n = []
            for j in range(1, w):
                buff = []
                for k in range(w):
                    if k != i:
                        buff.append(ma[j][k])
                n.append(buff)
            s *= -1
            res += mul * det(n, s * ma[0][i])
    return res

N = int(input('Введите размер квадратной матрицы: '))
m = np.arange(N*N)
for i in range(len(m)):
    m[i] = r.randint(-10, 10)
m = m.reshape(N, N)
print('Матрица:', m, sep='\n')
print('Детерминант матрицы: {}'.format(det(m)))
print('Детерминант матрицы, определённый функцией NumPy: {}'.format(int(np.linalg.det(m))))
