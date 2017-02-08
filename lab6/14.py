# Dyma Volodymyr KNIT16-A
# В основу древнеяпонского календаря был положен 60-летний цикл, состоящий из
# пяти 12-летних подциклов. Подциклы обозначались названиями цвета: зелёный,
# красный, желтый, белый и черный. Внутри каждого подцикла, годы носили
# названия животных: крысы, коровы, тигра, зайца, дракона, змеи, лошади,
# овцы, обезьяны, курицы, собаки и свиньи. 1984 год (год зеленой крысы) --
# начало очередного цикла.
# Разработать программу, которая вводит номер некоторого года нашей эры и
# печатает его название по древнеяпонскому календарю.

color = ['Green', 'Red', 'Yellow', 'White', 'Black']
animal = ['Rat', 'Cow', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse',
          'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig']

while True:
    start = 4
    flag = True
    try:
        year = int(input('Input a year: '))
        if year == 0:
            print(color[-1], animal[-4])
        elif year == 1:
            print(color[-1], animal[-3])
        elif year == 2:
            print(color[-1], animal[-2])
        elif year == 3:
            print(color[-1], animal[-1])
        elif year in range(4, 2018):
            while flag:
                for i in color:
                    for j in animal:
                        if year == start:
                            print(i, j)
                            flag = False
                            break
                        start += 1
                    if not flag:
                        break
        else:
            print('Year is out of current era.')
            continue
    except ValueError:
        print('The year must be an integer number!')
        continue
    if input('Press Enter to continue or input something to exit...') != '':
        exit()
