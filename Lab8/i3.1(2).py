# Дыма Владимир. КНИТ16-А
# Бинарный поиск

import numpy as np

r = int(input('Введите кол-во элементов массива: '))
A = np.arange(r+1)
l = int(input('Введите искомый элемент: '))
while r - l > 1:
    m = (l+r)
    if l < A[m]:
        r = m
    else:
        l = m
if A[l] == l:
    print('Элемент найден на позиции {}'.format(l))
else:
    print('Элемент не найден.')

