# Дыма Владимир. КНИТ16-А
# Алгоритм Бойера-Мура-Хорспула

from timeit import timeit

setup = '''
import numpy as np

d = input('Введите строку: ')
W = input('Введите искомую строку: ')
a = {i for i in d + W}
b = []
for i in a:
    b.append(ord(i))

a = max(b)
T = np.arange(a)
for i in range(0, a):
    T[i] = len(W)
for i in range(0, len(W)-1):
    T[ord(W[i])] = len(W) - 1 - i
'''

stmt = '''
skip = 0
while len(d) - skip >= len(W):
    i = len(W) - 1
    while d[skip + i] == W[i]:
        if i == 0:
            print(skip+1)
            exit()
        i -= 1
    skip += T[ord(d[skip + len(W) - 1])]
else:
    print('Nothing has been found.')
'''

print('Время выполнения: {} секунд.'.format(timeit(stmt, setup, number=1)))
