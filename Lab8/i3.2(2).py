# Дыма Владимир. КНИТ16-А
# Алгоритм Бойера-Мура-Хорспула

from timeit import timeit

setup = '''
text = input('Введите строку: ')
pattern = input('Введите искомую строку: ')
m = len(pattern)
n = len(text)
if m>n:
    print('Nothing was found.')

skip = [m] * (ord(max(max(text), max(pattern)))+1)
for k in range(m-1):
    skip[ord(pattern[k])] = m - k - 1
skip = tuple(skip)
'''

stmt = '''
k = m-1
while k < n:
    j = m - 1
    i = k
    while j >= 0 and text[i] == pattern[j]:
        j -= 1
        i -= 1
    if j == -1:
        print('String found at postition {}'.format(i+1))
        exit()
    k += skip[ord(text[k])]
else:
    print('Nothing has been found.')
'''

print('Время выполнения: {} секунд.'.format(timeit(stmt, setup, number=1)))
