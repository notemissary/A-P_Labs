# Дыма Владимир. КНИТ16-А
# Элементы линейного массива циклически сдвиньте на К позиций влево
# (без выполнения лишних сдвигов)

import numpy as np
import itertools

N = int(input('Введите длину массива: '))
K = int(input('Насколько сдвинуть массив? '))
m = np.arange(0, N)
print(m)
for j in range(K):
    v = m[0]
    for i in range(0, len(m)-1):
        c = i+1
        m[i] = m[c]
    m[c] = v
print(m)
