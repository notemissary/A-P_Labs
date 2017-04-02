# Дыма Владимир. КНИТ06-А
# Вычислите определитель квадратной матрицы (массива)

import numpy as np
import random as r


def det(matrix, mul=1):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            n = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                n.append(buff)
            sign *= -1
            total += mul * det(n, sign * matrix[0][i])
    return total

N = int(input('Введите размер квадратной матрицы: '))
m = np.arange(N*N)
for i in range(len(m)):
    m[i] = r.randint(-10, 10)
m = m.reshape(N, N)
print(m)
print(det(m))
