# Дыма Владимир. КНИТ16-А
# Повернуть квадратный массив ndarray на 90 градусов по часовой стрелке.

import numpy as np
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], int)
print(np.transpose(np.flip(m, 0), (1, 0)))
