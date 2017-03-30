# Дыма Владимир. КНИТ16-А
# Информация об изделиях на складе содержит данные о количестве в зависимости
# от размера детали и её цвета. Составить программу, которая позволит заносить
# и корректировать данные о наличии деталей на складе при поступлении новой
# партии деталей. При этом должна фиксироваться дата поступления деталей.

import numpy as np

DB = [['Красный', [1, 0], [2, 0], [3, 0]],
      ['Зелёный', [1, 0], [2, 0], [3, 0]],
      ['Синий', [1, 0], [2, 0], [3, 0]]]
story = []
while True:
    ch = int(input('Добро пожаловать! Выберите опцию:\n'
                   '1 - Добавить партию\n'
                   '2 - Удалить партию\n'
                   '3 - Просмотреть склад\n'
                   '4 - Просмотреть историю поступлений\n'
                   '0 - Выход\n'
                   '>> '))
    try:
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
            print('Успех! Добавлено {} деталей, цвета {}, размера {}.'
                  ''.format(adding[2], adding[0], adding[1]))
        elif ch == 2:
            deletion = input('Введите через запятую цвет детали, её размер и колличество: ')
            deletion = deletion.split(', ')
            try:
                deletion[2] = int(deletion[2])
            except IndexError:
                pass
            if deletion[0].lower() == DB[0][0].lower():
                if deletion[1] == 1:
                    if DB[0][1][1] >= deletion[2]:
                        DB[0][1][1] -= deletion[2]
                elif deletion[2] == 2:
                    if DB[0][2][1] >= deletion[2]:
                        DB[0][2][1] -= deletion[2]
                else:
                    if DB[0][3][1] >= deletion[2]:
                        DB[0][3][1] -= deletion[2]
            elif deletion[0].lower() == DB[1][0].lower():
                if deletion[1] == 1:
                    if DB[1][1][1] >= deletion[2]:
                        DB[1][1][1] -= deletion[2]
                elif deletion[2] == 2:
                    if DB[1][2][1] >= deletion[2]:
                        DB[1][2][1] -= deletion[2]
                else:
                    if DB[1][3][1] >= deletion[2]:
                        DB[1][3][1] -= deletion[2]
            elif deletion[0].lower() == DB[2][0].lower():
                if deletion[1] == 1:
                    if DB[2][1][1] >= deletion[2]:
                        DB[2][1][1] -= deletion[2]
                elif deletion[2] == 2:
                    if DB[2][2][1] >= deletion[2]:
                        DB[2][2][1] -= deletion[2]
                else:
                    if DB[2][3][1] >= deletion[2]:
                        DB[2][3][1] -= deletion[2]
            print('Успех! Удалено {} деталей, цвета {}, размера {}.'
                  ''.format(deletion[2], deletion[0], deletion[1]))
        elif ch == 3:
            print('============================================')
            for i in range(len(DB)):
                for j in range(1, len(DB) + 1):
                    print('{} деталь, рзмера {} в колличестве {} штук.'
                          ''.format(DB[i][0], DB[i][j][0], DB[i][j][1]))
            print('============================================')
        elif ch == 4:
            if len(story) != 0:
                for i in range(len(story)):
                    print('{}) '.format(i))
                    for j in story[i]:
                        print(j, end=', ')
            else:
                print('Ничего не поступало!')
        elif ch == 0:
            exit()
        else:
            print('Ошибка! Ха!')
    except IndexError:
        print('\nВы ввели что-то неверно! Введи снова.\n')
