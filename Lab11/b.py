# Дыма Владимир. КНИТ16-А
from string import ascii_letters
from random import shuffle

b = []
for i in ascii_letters:
    b.append(i)
shuffle(b)

print('Writing...')
f = open('in.txt', 'w')
for i in b:
    f.write(i)
f.close()

print('')
with open("in.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
