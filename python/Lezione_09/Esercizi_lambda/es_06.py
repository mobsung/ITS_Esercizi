'''
Usa reduce() (dal modulo functools) e una lambda per calcolare il prodotto di tutti gli elementi di una lista numeri = [2, 3, 4].
'''

from typing import Callable
from functools import reduce

numeri = [2, 3, 4]

print(reduce(lambda x, y: x * y, numeri))