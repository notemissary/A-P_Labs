# Dyma Volodymyr KNIT16-A
# В основу древнеяпонского календаря был положен 60-летний цикл, состоящий из
# пяти 12-летних подциклов. Подциклы обозначались названиями цвета: зелёный,
# красный, желтый, белый и черный. Внутри каждого подцикла, годы носили
# названия животных: крысы, коровы, тигра, зайца, дракона, змеи, лошади,
# овцы, обезьяны, курицы, собаки и свиньи. 1984 год (год зеленой крысы) --
# начало очередного цикла.
# Разработать программу, которая вводит номер некоторого года нашей эры и
# печатает его название по древнеяпонскому календарю.

from enum import Enum


class Color(Enum):
    Green = 1
    Red = 2
    Yellow = 3
    White = 4
    Black = 5


class Animal(Enum):
    Rat = 1
    Ox = 2
    Tiger = 3
    Rabbit = 4
    Dragon = 5
    Snake = 6
    Horse = 7
    Goat = 8
    Monkey = 9
    Rooster = 10
    Dog = 11
    Pig = 12

while True:
    start = 4
    try:
        year = int(input('Input a year: ')) % 60
        if year == 0:
            print(Color(4).name, Animal(9).name)
        elif year == 1:
            print(Color(4).name, Animal(10).name)
        elif year == 2:
            print(Color(5).name, Animal(11).name)
        elif year == 3:
            print(Color(5).name, Animal(12).name)
        else:
            c = 1
            flag = True
            while flag:
                for i in Color:
                    if start == year:
                        print(i.name, Animal(c).name)
                        flag = False
                        break
                    c += 1
                    start += 1
                    if c == 13:
                        c = 1
                    if start == year:
                        print(i.name, Animal(c).name)
                        flag = False
                        break
                    c += 1
                    start += 1
                    if c == 13:
                        c = 1
    except ValueError:
        print('The year must be an integer number!')
        continue
    if input('Press Enter to continue or input something to exit...') != '':
        exit()
