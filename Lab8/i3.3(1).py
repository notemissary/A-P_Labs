# Дыма Владимир. КНИТ16-А
# Информация об изделиях на складе содержит данные о количестве в зависимости
# от размера детали и её цвета. Составить программу, которая позволит заносить
# и корректировать данные о наличии деталей на складе при поступлении новой
# партии деталей. При этом должна фиксироваться дата поступления деталей.

import numpy as np

DB = [['Красный', [1, 0], [2, 0], [3, 0]],
      ['Зелёный', [1, 0], [2, 0], [3, 0]],
      ['Синий'], [1, 0], [2, 0], [3, 0]]
print(DB)
story = []
while True:
    ch = int(input('Добро пожаловать! Выберите опцию:\n'
                   '1 - Добавить партию\n'
                   '2 - Удалить партию\n'
                   '3 - Просмотреть склад\n'
                   '4 - Просмотреть историю поступлений\n'
                   '0 - Выход'))
    if ch == 1:
        adding = input('Введите через запятую цвет детали, её размер, колличество и '
                       'дату поступления: ')
        adding = adding.split(', ')
        story.append(adding)
        try:
            adding[2] = int(adding[2])
        except IndexError:
            pass
        if adding[0] == 'Красный':
            if adding[1] == 1:
                DB[0][1][1] += adding[2]
            elif adding[2] == 2:
                DB[0][2][1] += adding[2]
            else:
                DB[0][3][1] += adding[2]
        elif adding[0] == 'Зелёный':
            if adding[1] == 1:
                DB[1][1][1] += adding[2]
            elif adding[2] == 2:
                DB[1][2][1] += adding[2]
            else:
                DB[1][3][1] += adding[2]
        elif adding[0] == 'Синий':
            if adding[1] == 1:
                DB[2][1][1] += adding[2]
            elif adding[2] == 2:
                DB[2][2][1] += adding[2]
            else:
                DB[2][3][1] += adding[2]
    elif ch == 2:
        deletion = input('Введите через запятую цвет детали, её размер и колличество: ')
        deletion = deletion.split(', ')
        try:
            deletion[2] = int(deletion[2])
        except IndexError:
            pass
        if deletion[0] == 'Красный':
            if deletion[1] == 1:
                DB[0][1][1] -= deletion[2]
            elif deletion[2] == 2:
                DB[0][2][1] -= deletion[2]
            else:
                DB[0][3][1] -= deletion[2]
        elif deletion[0] == 'Зелёный':
            if deletion[1] == 1:
                DB[1][1][1] -= deletion[2]
            elif deletion[2] == 2:
                DB[1][2][1] -= deletion[2]
            else:
                DB[1][3][1] -= deletion[2]
        elif deletion[0] == 'Синий':
            if deletion[1] == 1:
                DB[2][1][1] -= deletion[2]
            elif deletion[2] == 2:
                DB[2][2][1] -= deletion[2]
            else:
                DB[2][3][1] -= deletion[2]
    elif ch == 3:
        print(DB)
    elif ch == 4:
        print(story)
    elif ch == 0:
        exit()
    else:
        print('Ошибка! Ха!')
