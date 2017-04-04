# Дыма Владимир. КНИТ16-А
# Информация об изделиях на складе содержит данные о количестве в зависимости
# от размера детали и её цвета. Составить программу, которая позволит заносить
# и корректировать данные о наличии деталей на складе при поступлении новой
# партии деталей. При этом должна фиксироваться дата поступления деталей.

from enum import Enum


class Color(Enum):
    Red = 0
    Green = 1
    Blue = 2

DB = [['Красный', [1, 0], [2, 0], [3, 0]],
      ['Зелёный', [1, 0], [2, 0], [3, 0]],
      ['Синий', [1, 0], [2, 0], [3, 0]]]
story = []
while True:
    try:
        ch = int(input('Добро пожаловать! Выберите опцию:\n'
                       '1 - Добавить партию\n'
                       '2 - Удалить партию\n'
                       '3 - Просмотреть склад\n'
                       '4 - Просмотреть историю поступлений\n'
                       '0 - Выход\n'
                       '>> '))
    except ValueError:
        print('Ошибка ввода. Введите число!')
        continue
    try:
        if ch == 1:
            adding = input('Введите через запятую цвет детали, её размер, колличество и '
                           'дату поступления: ')
            adding = adding.split(', ')
            try:
                adding[2] = int(adding[2])
                if len(adding) == 4:
                    story.append(adding)
            except IndexError:
                print('Ошибка, введены некорректные данные.')
            if adding[0].lower() == DB[0][0].lower():
                if adding[1] == 1:
                    DB[0][1][1] += adding[2]
                elif adding[1] == 2:
                    DB[0][2][1] += adding[2]
                else:
                    DB[0][3][1] += adding[2]
            elif adding[0].lower() == DB[1][0].lower():
                if adding[1] == 1:
                    DB[1][1][1] += adding[2]
                elif adding[1] == 2:
                    DB[1][2][1] += adding[2]
                else:
                    DB[1][3][1] += adding[2]
            elif adding[0].lower() == DB[2][0].lower():
                if adding[1] == 1:
                    DB[2][1][1] += adding[2]
                elif adding[1] == 2:
                    DB[2][2][1] += adding[2]
                else:
                    DB[2][3][1] += adding[2]
            print('\nУспех! Добавлено {} деталей, цвета {}, размера {}.'
                  '\n'.format(adding[2], adding[0], adding[1]))
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
                    else:
                        print('Нельзя удалить больше, чем есть.')
                elif deletion[1] == 2:
                    if DB[0][2][1] >= deletion[2]:
                        DB[0][2][1] -= deletion[2]
                    else:
                        print('Нельзя удалить больше, чем есть.')
                else:
                    if DB[0][3][1] >= deletion[2]:
                        DB[0][3][1] -= deletion[2]
                    else:
                        print('Нельзя удалить больше, чем есть.')
            elif deletion[0].lower() == DB[1][0].lower():
                if deletion[1] == 1:
                    if DB[1][1][1] >= deletion[2]:
                        DB[1][1][1] -= deletion[2]
                    else:
                        print('Нельзя удалить больше, чем есть.')
                elif deletion[1] == 2:
                    if DB[1][2][1] >= deletion[2]:
                        DB[1][2][1] -= deletion[2]
                    else:
                        print('Нельзя удалить больше, чем есть.')
                else:
                    if DB[1][3][1] >= deletion[2]:
                        DB[1][3][1] -= deletion[2]
                    else:
                        print('Нельзя удалить больше, чем есть.')
            elif deletion[0].lower() == DB[2][0].lower():
                if deletion[1] == 1:
                    if DB[2][1][1] >= deletion[2]:
                        DB[2][1][1] -= deletion[2]
                    else:
                        print('Нельзя удалить больше, чем есть.')
                elif deletion[1] == 2:
                    if DB[2][2][1] >= deletion[2]:
                        DB[2][2][1] -= deletion[2]
                    else:
                        print('Нельзя удалить больше, чем есть.')
                else:
                    if DB[2][3][1] >= deletion[2]:
                        DB[2][3][1] -= deletion[2]
                    else:
                        print('Нельзя удалить больше, чем есть.')
            print('\nУспех! Удалено {} деталей, цвета {}, размера {}.'
                  '\n'.format(deletion[2], deletion[0], deletion[1]))
        elif ch == 3:
            print('============================================')
            for i in range(len(DB)):
                for j in range(1, len(DB) + 1):
                    print('{} деталь, рзмера {} в колличестве {} штук.'
                          ''.format(DB[i][0], DB[i][j][0], DB[i][j][1]))
            print('============================================')
        elif ch == 4:
            if len(story) != 0:
                print('==================История==================')
                for i in range(len(story)):
                    print('{})'.format(i), end=' ')
                    for j in story[i]:
                        print(j, end=', ')
                print('\n============================================')
            else:
                print('\nНичего не поступало!\n')
        elif ch == 0:
            exit()
        else:
            print('\nОшибка! Ха!\n')
    except IndexError:
        print('\nВы ввели что-то неверно! Введи снова.\n')
