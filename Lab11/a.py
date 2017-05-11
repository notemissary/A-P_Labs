# Дыма Владимир. КНИТ16-А
from array import array
from random import random
from pickle import dump, load
a = [round(i*random(), 2) for i in range(-5, 6)]
a.remove(0)
a = array('d', a)

dump(a, open('buka.b', 'wb'))

b = list(load(open('buka.b', 'rb')))

print(b)
print('Summa: {}'.format(sum(b)))
r = 1
for i in b:
    r *= i
print('Multiplication: {}'.format(r))
r = 0
for i in b:
    r += i**2
print('Summ of square: {}'.format(r))
print('Sum module: {}'.format(abs(sum(b))))
for i in b:
    r *= i
print('Multiplication square: {}'.format(r**2))
print('The last element: {}'.format(b.pop()))
