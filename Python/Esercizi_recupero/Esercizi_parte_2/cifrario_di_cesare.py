'''
Il cifrario di Cesare è un antico metodo crittografico che rende alcune informazioni nascoste
a chi non possiede la chiave per decifrarle.
Immagina l'alfabeto come una lista ordinata di lettere (puoi importare la lista delle lettere
dell'alfabeto minuscole scrivendo from string import ascii_lowercase
Ogni lettera ha una posizione in questa lista:
● a è 1
● b è 2
● j è 10
● e così via…
Il cifrario di Cesare nasconde l'informazione utilizzando una chiave, che è un numero intero
positivo, da sommare alla posizione della lettera originale: il risultato ottenuto corrisponde
alla posizione della lettera cifrata.

● a con key = 2 diventa c
Se la chiave porta oltre la fine dell'alfabeto, si ricomincia dal principio:

● a con key = 28 diventa c
Per decriptare (o “decifrare”) il messaggio, si applica la stessa procedura ma muovendosi
all'indietro nell'alfabeto. Devi fornire le funzioni:
caesar_cypher_encrypt(s, key)
caesar_cypher_decrypt(s, key)
dove:
● s è una stringa (lettera, parola, frase, ecc.).

● key è un numero intero positivo, la chiave del cifrario di Cesare.
La tua implementazione deve trasformare soltanto le lettere ASCII maiuscole e minuscole.
Caratteri speciali, numeri e lettere accentate non devono essere modificati.
Le funzioni non devono stampare nulla a schermo, ma restituire la stringa cifrata o
decifrata.
'''

from string import ascii_lowercase

def caesar_cypher_encrypt(word: str, key: int) -> str:

    alpha: str = ascii_lowercase
    crypted_word: str = ''

    for char in word:
        if char.isalpha():
            
            upp: bool = True if char.isupper() else False

            for index, letter in enumerate(alpha):
                if char.lower() == letter:
                    pos: int = (index + key) % len(alpha)

            crypted_word += alpha[pos].upper() if upp == True else alpha[pos]

        else:
            crypted_word += char

    return crypted_word

def caesar_cypher_decrypt(word: str, key: int) -> str:

    alpha: str = ascii_lowercase
    decrypted_word: str = ''

    for char in word:
        if char.isalpha():

            upp: bool = True if char.isupper() else False

            for index, letter in enumerate(alpha):
                if char.lower() == letter:
                    pos: int = index - (key % len(alpha))
            
            decrypted_word += alpha[pos].upper() if upp == True else alpha[pos]

        else:
            decrypted_word += char

    return decrypted_word

print(caesar_cypher_encrypt('stefano', 40))
print(caesar_cypher_decrypt('gHsToBc', 40))
            