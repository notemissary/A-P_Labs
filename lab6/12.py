# Dyma Volodymyr KNIT16-A
# Значение переменной x, обозначающую некоторую длину в единицах p, заменить
# величиной этой же длины в метрах.

from enum import Enum


class Measure(Enum):
    decimetre = 0.1
    kilometre = 1000
    metre = 1
    millimetre = 0.001
    centimetre = 0.01

x = float(input('Length: '))
p = Measure[input('Measure: ')]

print(x * p.value, 'метров.')
