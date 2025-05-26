
from myTypes import IntGEZ

class Citta:

    _name: str
    _population: IntGEZ

    def __init__(self, name: str, population: int | IntGEZ | str | bool | float) -> None:
        self._name = name
        self._population = IntGEZ(population)

    def __str__(self) -> str:
        return f'City name: {self._name} - Current population: {self._population}'


if __name__ == '__main__':

    roma: Citta = Citta('roma', 10)
    print(roma)