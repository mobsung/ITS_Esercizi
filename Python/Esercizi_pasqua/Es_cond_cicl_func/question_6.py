'''
Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.

Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.

For example:

Test	                        Result
print(hypotenuse(3.0, 4.0))     -> 5.0

print(hypotenuse(8.0, 15.0))    -> 17.0
'''

import math

def hypotenuse(lato_1:float, lato_2:float) -> float:

    return math.sqrt((lato_1 ** 2) + (lato_2 ** 2))


if __name__ == "__main__":
    print(hypotenuse(3.0, 4.0))
    print(hypotenuse(8.0, 15.0))