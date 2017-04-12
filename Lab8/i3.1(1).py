# Дыма Владимир. КНИТ16-А
# Линейный поиск

# from timeit import timeit

# setup = '''
import numpy as np

l = int(input('Введите длину массива: '))
arr = np.arange(l+1)
x = int(input('Введите искомый элемент: '))
# '''

# stmt = '''
i = 0
while True:
    if arr[i] == x:
        print('Успех! {} элемент на позиции {}'.format(x, i+1))
        break
    else:
        i += 1
        if i == l+1:
            print('Провал! Элемент {} не найден.'.format(x))
            break
# '''

# print('Время выполнения: {} '.format(timeit(stmt, setup, number=1)))
