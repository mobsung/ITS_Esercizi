from creatura import Creatura
from mostro import Mostro
from alieno import Alieno
from funzioni import *


if __name__ == '__main__':

    alieno1: Alieno = Alieno(nome='Robot')
    mostro1: Mostro = Mostro(nome='godzilla', urlo='Wazaa!', gemito='Nooooo!')

    proclamaVincitore(combattimento(a=alieno1, m=mostro1))
