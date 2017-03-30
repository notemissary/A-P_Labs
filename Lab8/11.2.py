# Дыма Владимир. КНИТ16-А
# Элементы линейного массива циклически сдвиньте на К позиций влево
# (без выполнения лишних сдвигов)

import numpy as np
import itertools

K = int(input('Насколько сдвинуть массив? '))
m = np.arange(0, 10).ravel()
b = np.broadcast(K, 0)
s = {ax: 0 for ax in range(m.ndim)}
for sh, ax in b:
    if -m.ndim <= ax < m.ndim:
        s[ax % m.ndim] += sh
rolls = [((slice(None), slice(None)),)] * m.ndim
res = np.empty_like(m)
for ax, offset in s.items():
    offset %= m.shape[ax] or 1
    if offset:
        rolls[ax] = ((slice(None, -offset), slice(offset, None)),
                     (slice(-offset, None), slice(None, offset)))
    for indicies in itertools.product(*rolls):
        arr_index, res_index = zip(*indicies)
        res[res_index] = m[arr_index]

print(res)
