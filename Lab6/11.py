# Dyma Volodymyr, KNIT16-A
# По дате d, m, y определить дату следующего дня

days = range(1, 32)
months = range(1, 13)
years = range(1901, 2017)

while True:
    try:
        d, m, y = int(input('День: ')), int(input('Месяц: ')), \
                  int(input('Год: '))
        if d in days and m in months and y in years:
            if m == 2 and (y % 4 == 0):
                if d in range(1, 29):
                    print('{}/{}/{}'.format(d + 1, m, y))
                elif d == 29:
                    print('{}/{}/{}'.format(1, m + 1, y))
                else:
                    print('Out of range.')
            elif m == 2:
                if d in range(1, 28):
                    print('{}/{}/{}'.format(d + 1, m, y))
                elif d == 28:
                    print('{}/{}/{}'.format(1, m + 1, y))
                else:
                    print('Out of range!')
            elif m in {4, 6, 9, 11}:
                if d in range(1, 30):
                    print('{}/{}/{}'.format(d + 1, m, y))
                elif d == 30:
                    print('{}/{}/{}'.format(1, m + 1, y))
                else:
                    print('Out of range!')
            elif m in {1, 3, 5, 7, 8, 10, 12}:
                if d in range(1, 31):
                    print('{}/{}/{}'.format(d + 1, m, y))
                elif d == 31:
                    print('{}/{}/{}'.format(1, m + 1, y))
        else:
            print('Out of range!')
    except ValueError:
        print('Значения должны быть целочисленными!')
        continue
    if input('Нажмите Enter, чтобы продолжить, либо введите '
             'что-то для выхода') != '':
        break
