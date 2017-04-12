# Дыма Владимир. КНИТ16-А
# Алгоритм Кнута-Морриса-Пратта

# from timeit import timeit

# setup = '''
d = input('Введите строку: ')
W = input('Введите искомую подстроку: ')

T = [0] * len(W)
T[0] = -1
T[1] = 0
pos = 2
cnd = 0
while pos < len(W):
    if W[pos-1] == W[cnd]:
        cnd += 1
        T[pos] = cnd
        pos += 1
    elif cnd > 0:
        cnd = T[cnd]
    else:
        T[pos] = 0
        pos += 1
# '''

# stmt = '''
m = 0
i = 0
while m+i < len(d):
    if W[i] == d[m+i]:
        if i == len(W)-1:
            print('Успех! Подстрока найдена на позиции {}.'.format(m+1))
            break
        i += 1
    else:
        if T[i] > -1:
            m += i - T[i]
            i = T[i]
        else:
            m += 1
            i = 0
else:
    print('Провал! Подстрока не найдена.')
# '''

# print('Время выполнения: {} секунд.'.format(timeit(stmt, setup, number=1)))
