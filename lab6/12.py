# Dyma Volodymyr KNIT16-A
# Значение переменной x, обозначающую некоторую длину в единицах p, заменить
# величиной этой же длины в метрах.

from enum import Enum


class measure(Enum):
    decimetre = 1
    kilometre = 2
    metre = 3
    millimetre = 4
    centimetre = 5


x = float(input('Length: '))
p = measure[input('Measure: ')]
