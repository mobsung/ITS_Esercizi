'''
Scrivere un programma PYTHON che a partire da una stringa la cifra con la tecnica XOR
Successivamente mostrare che la stringa cifrata, riapplicando lo stesso XOR, torna la stringa originale
Per fare lo XOR utilizzate un solo valore: 57
Quindi data la stringa di esempio “Nel mezzo del cammin di nostra vita”, dovete fare per ogni carattere della stringa lo xor con il valore 57
“N” xor 57, “e” xor 57, …
Ottenendo una lista di numeri es: 78 (che è il codice asciii  della lettera N) xor (si indica con il simbolo ^) => 78 ^ 57 = 119
E così via per tutta la stringa.
Al termine stampare la lista di numeri ottenuti
In fondo a partire dalla lista di numeri, riapplicare lo xor sempre con 57 e quindi ottenere (ricostruendola) la stringa originale
NB: potreste utilizzare input(“…”) in modo da leggere sia la stringa da cifrare, sia il valore segreto da applicare come xor
'''

from functools import reduce

word: str = input('Scrivi la frase da codificare\n==> ')
key: int = int(input('Inserisci un intero come chiave di codifica\n==> '))

cifrato: list[int] = [ord(char) ^ key for char in word]

print(cifrato)

decifrato: str = ''.join([chr(char ^ key) for char in cifrato])

print(decifrato)


#================================================================================================

cifrato = list(map(lambda c: ord(c) ^ key, list(word)))

decifrato = reduce(lambda x,y: x+y, map(lambda x : chr(x ^ key), cifrato), "")

print(cifrato, decifrato)