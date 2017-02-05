# Dyma Volodymyr, KNIT16-A
# По дате d, m, y определить дату следующего дня

days = range(1, 32)
months = range(1, 13)
years = range(1901, 2016)
d, m, y = int(input()), int(input()), int(input())
if d == 31:
    if m == 12:
        print('01/01', y + 1, sep='/')
    else:
        print('01', m + 1, y, sep='/')
else:
    print(d + 1, m, y, sep='/')
