# Дыма Владимир. КНИТ16-А
# Алгоритм Бойера-Мура-Хорспула

import numpy as np

haystack = input('Введите строку: ')
needle = input('Введите искомую строку: ')

T = np.arange(2048)
for i in range(0, 256):
    T[i] = len(needle)
for i in range(0, len(needle)-1):
    T[ord(needle[i])] = len(needle) - 1 - i


skip = 0
while len(haystack) - skip >= len(needle):
    i = len(needle) - 1
    while haystack[skip + i] == needle[i]:
        if i == 0:
            print(skip+1)
        i -= 1
    skip += T[ord(haystack[skip + len(needle)-1])]
else:
    print('Nothing has been found.')
