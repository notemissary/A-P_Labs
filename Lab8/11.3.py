# Дыма Владимир. КНИТ16-А
# Выполнить произведение двух квадратных матриц (массивов), учесть размерность

import numpy as np

m = np.ones((3, 3))
n = np.ones((3, 3))
for i in range(3):
    for j in range(3):
        m[i][j] = int(input('Введите элемент m[{}][{}]: '.format(i+1, j+1)))
for i in range(3):
    for j in range(3):
        n[i][j] = int(input('Введите элемент n[{}][{}]: '.format(i+1, j+1)))
print(np.asanyarray([[sum(a*b for a, b in zip(m_row, n_col)) for n_col in zip(*n)] for m_row in m]))
