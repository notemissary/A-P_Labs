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


s = Country[input('Country: ')]
print(Continent(s.value).name)
