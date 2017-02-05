# Dyma Volodymyr KNIT16-A
# Значение переменной x, обозначающую некоторую длину в единицах p, заменить
# величиной этой же длины в метрах.

from enum import Enum


class Measure(Enum):
    decimeter = 0.1
    kilometer = 1000
    meter = 1
    millimeter = 0.001
    centimeter = 0.01


while True:
    try:
        x = float(input('Length: '))
        p = Measure[input('Measure: ')]
        print('{} meters.'.format(x * p.value))
    except (ValueError, KeyError):
        print('Wrong value or key.')
        continue
    if input('Press Enter to continue or input something to exit') != '':
        exit()
