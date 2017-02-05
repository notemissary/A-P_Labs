# Dyma Volodymyr KNIT16-A
# По названию s-страны определить название её континента.

from enum import Enum


class Country(Enum):
    Germany = 3
    Cuba = 2
    Laos = 1
    Monaco = 3
    Bangladesh = 1
    Ukraine = 3


class Continent(Enum):
    Asia = 1
    America = 2
    Europe = 3


while True:
    try:
        s = Country[input('Country: ')]
        print(Continent(s.value).name)
    except KeyError:
        print('Country has not found.')
    if input('Press Enter to continue or input something to exit') != '':
        exit()
