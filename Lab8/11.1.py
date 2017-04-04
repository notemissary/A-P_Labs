# Дыма Владимир. КНИТ16-А
# Повернуть квадратный массив ndarray на 90 градусов по часовой стрелке.

import numpy as np

N = int(input('Введите размер матрицы: '))

m = np.arange(N*N).reshape((N, N))
m = m[::-1]
for i in range(len(m)):
        for j in range(i+1, len(m[i])):
            m[i][j], m[j][i] = m[j][i], m[i][j]
print(m)
