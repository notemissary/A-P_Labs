# Dyma Volodymyr KNIT16-A
# Значение переменной x, обозначающую некоторую длину в единицах p, заменить
# величиной этой же длины в метрах.

from enum import Enum


class Measure(Enum):
    decimeter = 1
    kilometer = 2
    meter = 3
    millimeter = 4
    centimeter = 5

while True:
    try:
        x = float(input('Length: '))
        p = Measure[input('Measure: ')].value
        if p == 1:
            x /= 10
        elif p == 2:
            x *= 1000
        elif p == 4:
            x /= 1000
        elif p == 5:
            x /= 100
        print('{} meters.'.format(x))
    except (ValueError, KeyError):
        print('Wrong value or key.')
        continue
    if input('Press Enter to continue or input something to exit') != '':
        exit()
