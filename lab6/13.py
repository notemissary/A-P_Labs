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


s = Country[input('Country: ')]
