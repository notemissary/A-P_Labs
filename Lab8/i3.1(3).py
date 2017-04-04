# Дыма Владимир. КНИТ16-А
# Прямой поиск подстроки

from timeit import timeit

setup = '''
s = input('Введите строку: ')
ss = input('Введите искомую подстроку: ')
ls = len(s)
lss = len(ss)
I = 1
c = 0
'''

stmt = '''
while c < lss:
    if s[I-1] == ss[c]:
        I += 1
        c += 1
    else:
        c = 0
        I += 1
        break
    if ls < c + I:
        print('Элемент не нейден.')
        exit()
else:
    print('Успех! Подстрока начинается с позиции {}'.format(I - 1))
'''

print('Время выполнения: {} '.format(timeit(stmt, setup, number=1)))
