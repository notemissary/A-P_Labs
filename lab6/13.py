# Dyma Volodymyr KNIT16-A
# По названию s-страны определить название её континента.

from enum import Enum


class Country(Enum):
    Germany = 1
    Cuba = 2
    Laos = 3
    Monaco = 4
    Bangladesh = 5
    Ukraine = 6


class Continent(Enum):
    Asia = 1
    America = 2
    Europe = 3

while True:
    try:
        s = Country[input('Country: ')].value
        if s == 1:
            continent = Continent(3)
        elif s == 2:
            continent = Continent(2)
        elif s == 3:
            continent = Continent(1)
        elif s == 4:
            continent = Continent(3)
        elif s == 5:
            continent = Continent(1)
        else:
            continent = Continent(3)
        print('{}'.format(continent.name))
    except KeyError:
        print('Country has not found.')
    if input('Press Enter to continue or input something to exit') != '':
        exit()
