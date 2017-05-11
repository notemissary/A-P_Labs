# Дыма Владимир. КНИТ16-А
from array import array
from random import random

a = array('d', [i*random() for i in range(10)])

f = open('buka', 'wb+')
a.tofile(f)
f.close()

f = open('buka', 'r')
k = array('d')
k.fromstring(f.read())