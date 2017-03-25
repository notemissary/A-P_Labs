# Дыма Владимир. КНИТ16-А
# Повернуть квадратный массив ndarray на 90 градусов по часовой стрелке.

import numpy as np
m = np.array([[1, 2], [3, 4]], int)
print(m, 'Rotating...', np.rot90(m, axes=(1, 0)), sep='\n\n')
