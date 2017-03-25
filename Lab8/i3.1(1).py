# Дыма Владимир. КНИТ16-А
# Линейный поиск

import numpy as np

len = int(input('Введите длину массива: '))
arr = np.arange(len + 1)
x = int(input('Введите искомый элемент: '))
i = 0
while True:
    if arr[i] == x:
        print('Успех! {} элемент на позиции {}'.format(x, i+1))
        break
    else:
        i += 1
        if i == len+1:
            print('Провал! Элемент {} не найден.'.format(x))
            break