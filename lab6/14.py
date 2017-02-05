# Dyma Volodymyr KNIT16-A
# В основу древнеяпонского календаря был положен 60-летний цикл, состоящий из
# пяти 12-летних подциклов. Подциклы обозначались названиями цвета: зелёный,
# красный, желтый, белый и черный. Внутри каждого подцикла, годы носили
# названия животных: крысы, коровы, тигра, зайца, драковна, змеи, лошади,
# овцы, обезьяны, курицы, собаки и свиньи. 1984 год (год зеленой крысы) --
# начало очередного цикла.
# Разработать программу, которая вводит номер некоторого года нашей эры и
# печатает его название по древнеяпонскому календарю.

color = ['Green', 'Red', 'Yellow', 'White', 'Black']
animal = ['Rat', 'Cow', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse',
          'Sheep', 'Monkey', 'Chicken', 'Dog', 'Pig']

while True:
    start = -56
    flag = True
    try:
        n = int(input('Input a year: '))
        while flag:
            for i in color:
                for j in animal:
                    if n == start:
                        print(i, j)
                        flag = False
                        break
                    start += 1
                if not flag:
                    break
    except ValueError:
        print('The year must be an integer number!')
        continue
    if input('Press Enter to continue or input something to exit') != '':
        exit()
