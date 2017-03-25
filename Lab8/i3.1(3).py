# Дыма Владимир. КНИТ16-А
# Прямой поиск подстроки

s = input('Введите строку: ')
ss = input('Введите искомую подстроку: ')
ls = len(s)
lss = len(ss)
I = 1
while I < ls:
    c = 0
    while True:
        if s[I-1] == ss[c]:
            I += 1
            c += 1
        else:
            break
        if c == lss-1:
            print('Успех! Подстрока начинается с позиции {}'.format(I-1))
            exit()
    I += 1
else:
    print('Подстрока не найдена!')
