# Dyma Volodymyr, KNIT16-A
# По дате d, m, y определить дату следующего дня

days = range(1, 32)
months = range(1, 13)
m30 = [4, 6, 9, 11]
years = range(1901, 2017)
feb = range(1, 29)
leap_year = range(1900, 2017, 4)
leap_feb = range(1, 30)

while True:
    try:
        d, m, y = int(input('День: ')), int(input('Месяц: ')), \
                  int(input('Год: '))
        if y in years and m in months and d in days:
            if y in leap_year:
                if m == 2:
                    if d in leap_feb:
                        if d == 29:
                            print(1, m + 1, y, sep='/')
                        else:
                            print(d + 1, m, y, sep='/')
                    else:
                        print(y, '- високосный год. В феврале 29 дней.')
                        continue
            if m != 2:
                if m in m30:
                    if d == 30:
                        if m == 12:
                            print('1/1', y + 1, sep='/')
                        else:
                            print(1, m + 1, y, sep='/')
                    else:
                        print(d + 1, m, y, sep='/')
                else:
                    if d == 30:
                        if m == 12:
                            print('1/1', y + 1, sep='/')
                        else:
                            print(1, m + 1, y, sep='/')
                    else:
                        print(d + 1, m, y, sep='/')
            else:
                if y not in leap_year:
                    if d in feb:
                        if d == 28:
                            if m == 12:
                                print('1/1', y + 1, sep='/')
                            else:
                                print(1, m + 1, y + 1, sep='/')
                        else:
                            print(d + 1, m, y, sep='/')
                    else:
                        print('В феврале невисокосного года 28 дней.')
                        continue
        else:
            print('Значения вне допустимого диапазона!')
            continue
    except ValueError:
        print('Значения должны быть целочисленными!')
        continue
    if input('Нажмите Enter, чтобы продолжить, либо введите '
             'что-то для выхода') != '':
        break
