# Дыма Владимир. КНИТ16-А
# Бинарный поиск

import numpy as np

n = int(input('Введите кол-во элементов массива: '))
A = np.arange(n+1)
T = int(input('Введите искомый элемент: '))
L = 0
R = n
while True:
    if L > R:
        print('Неудача! Элемент {} не найден.'.format(T))
        break
    else:
        m = int((L + R)/2)
        if A[m] < T:
            L = m + 1
            continue
        elif A[m] > T:
            R = m - 1
            continue
        else:
            print('Успех! Элемент {} найден на позиции {}.'.format(T, m+1))
            break
