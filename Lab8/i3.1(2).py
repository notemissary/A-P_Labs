# Дыма Владимир. КНИТ16-А
# Бинарный поиск

from timeit import timeit

setup = '''
import numpy as np

r = int(input('Введите кол-во элементов массива: '))
A = np.arange(r+1)
l = int(input('Введите искомый элемент: '))
'''

stmt = '''
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
'''

print('Время выполнения: {} '.format(timeit(stmt, setup, number=1)))
