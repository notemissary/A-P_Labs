from numpy import zeros, random
from pickle import dump, loads


def dijkstra(s, n, a):
    wt_bool = [True] * n  # принадлежности элемента множеству wt
    wt = [100] * n  # множество посещённых вершин
    wt[s] = 0  # установка нулевого(начального) элемента
    for i in range(n):
        min_wt = 101  # максимально возможное число длины пути
        id_min_wt = -1  # индекс минимального расстояния
        for i in range(len(wt)):
            if wt_bool[i] and wt[i] < min_wt:
                min_wt = wt[i]
                id_min_wt = i
        for i in range(n):
            if wt[id_min_wt] + a[id_min_wt][i] < wt[i]:
                wt[i] = wt[id_min_wt] + a[id_min_wt][i]
        wt_bool[id_min_wt] = False
    return wt


while True:
    try:
        num_cities = int(input('Please enter the amount of cities\n> '))
        if num_cities < 2:
            print('The amount of cities can not be  less than 2!\n')
            continue
    except ValueError:
        print('Please enter integer number!\n')
        continue
    while True:
        try:
            start_city = int(input('\nEnter the number of the initial city\n'
                                   'From 1 to {} \n> '.format(num_cities)))
            if start_city - 1 not in range(0, num_cities):
                print('Please enter a number from the range!\n')
                continue
            break
        except ValueError:
            print('Please enter an integer number!\n')
            continue
    while True:
        fill_arr = input('\nHow do you want input the length of the roads '
                         'between the cities?\n 1 - Random\n 2 - Manual\n> ')
        if fill_arr == '1':
            arr_of_len = random.randint(1, 100, (num_cities, num_cities))
            break
        elif fill_arr == '2':
            while True:
                arr_of_len = zeros((num_cities, num_cities), dtype=int)
                flag = False
                for i in range(0, num_cities):
                    arr_of_len[i][i] = 0
                    for j in range(i + 1, num_cities):
                        try:
                            inp = int(input('\nEnter the distance between the '
                                            'city {} and the city {}\n> '
                                            ''.format(i + 1, j + 1)))
                            if inp == 0:
                                inp = 100
                            elif inp > 99:
                                print('The road length can\'t be bigger than '
                                      '100!\n')
                                flag = True
                                break
                            arr_of_len[i][j], arr_of_len[j][i] = inp, inp
                        except ValueError:
                            print('Please enter an integer number!\n')
                            flag = True
                            break
                    if flag:
                        break
                if not flag:
                    break
            break
        else:
            print('Please enter a correct number!\n')
            continue
    file = open('res.txt', 'wb')
    dump(arr_of_len, file)
    file.close()
    file_bin_arr = open('res.txt', 'rb')
    f = file_bin_arr.read()
    print('\nThe system of the roads defined by the matrix\n{}\n'
          .format(loads(f)))
    returned = dijkstra(start_city - 1, num_cities, loads(f))
    for i in range(len(returned)):
        if i == start_city - 1:
            continue
        print('Length from the city {} to the city {}: {}'
              .format(start_city, i + 1, returned[i]))
    file_bin_arr.close()
    ask = input('\nDo you want try again? [y/n]: ')
    if ask == 'y':
        continue
    else:
        break
