# Dyma Volodymyr. KNIT16-A
# Написать программу вычислени суммы тех элементов матрицы a, номера строк и
# столбцов которых принадлежат соответсвенно непутым множествам s_1 и s_2.

while True:
    n = 10
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    s_1 = {i for i in range(n)}
    s_2 = {i for i in range(n)}
    print(sum(value for row_id, row in enumerate(a) if row_id in s_1
              for col_id, value in enumerate(row) if col_id in s_2))
    if input('Press Enter to continue...') != '':
        break
