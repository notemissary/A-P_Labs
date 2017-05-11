# Дыма Владимир. КНИТ16-А
import numpy as np


def dijkstra(s, n, a):
    wt_bool = [True] * n  # принадлежности элемента множеству wt
    wt = [50] * n  # множество посещённых вершин
    wt[s] = 0  # установка нулевого(начального) элемента
    for i in range(n):
        min_wt = 51  # максимально возможное число длины пути
        id_min_wt = -1  # индекс минимального расстояния
        for j in range(len(wt)):
            if wt_bool[j] and wt[j] < min_wt:
                min_wt = wt[j]
                id_min_wt = j
        for j in range(n):
            if wt[id_min_wt] + a[id_min_wt][j] < wt[j]:
                wt[j] = wt[id_min_wt] + a[id_min_wt][j]
        wt_bool[id_min_wt] = False
    return wt

# d = dijkstra(1, len(a), a)
# print(d)
# for i in range(len(d)):
#     if i == 1:
#         continue
#     print('Len from city 2 to city {} → {}'.format(i+1, d[i]))

while True:
    try:
        num_cities = int(input('Please enter the number of cities\n> '))
        if num_cities < 2:
            print('Number of cities can not be less than 2!\n')
            continue
    except ValueError:
        print('Please enter integer number!\n')
        continue
    while True:
        try:
            start_city = int(input('Enter the number of the initial city\nFrom '
                                   '1 to {}\n> '.format(num_cities)))
            if start_city - 1 not in range(0, num_cities):
                print('Please enter a number from the range!\n')
                continue
            break
        except ValueError:
            print('Please enter integer number!\n')
            continue
    while True:
        fill_arr = input('How do you want input the length of the roads between '
                         'cities?\n 1 -- Random\n 2 -- Manual\n> ')
        if fill_arr == '1':
            arr_of_len = np.random.randint(1, 51, (num_cities, num_cities))
            break
        elif fill_arr == '2':
            arr_of_len = np.zeros((num_cities, num_cities), dtype = int)
            flag = False
            for i in range(0, num_cities):
                arr_of_len[i][i] = 0
                for j in range(i + 1, num_cities):
                    try:
                        inp = int(input('Enter the distance between city {} and '
                                        'city {}\n> '.format(i + 1, j + 1)))
                        arr_of_len[i][j], arr_of_len[j][i] = inp, inp
                    except ValueError:
                        print('Please enter integer number!')
                        flag = True
                        break
                if flag:
                    break
            break
        else:
            print('You did it wrong!')

