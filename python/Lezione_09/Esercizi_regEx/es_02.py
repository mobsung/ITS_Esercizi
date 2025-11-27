'''
2. Riconoscere parole
Obiettivo: Lavorare con lettere e lunghezze di stringhe.

Esercizio 2.1: Scrivi una RegEx che riconosca una parola composta solo da lettere minuscole.
Esercizio 2.2: Adatta la RegEx per accettare parole con lettere maiuscole e minuscole.
Esercizio 2.3: Modifica la RegEx per accettare parole lunghe da 5 a 10 caratteri.
'''

import re

# test only Upper # re.fullmatch(r'[A-Z]+', text)
def isUpper(text:str) -> None:

    print(True if re.fullmatch(r'[A-Z]+', text) else False)

# "ABC" expecterd # True
isUpper("ABC")

# "abc" expecterd # False
isUpper("abc")

# "ABC" expecterd # False
isUpper("Abc")


# test Upper and Lower # re.fullmatch(r'[A-Za-z]+', text)
def isUpperLower(text:str) -> None:

    print(True if re.fullmatch(r'[A-Za-z]+', text) else False)

# "ABC" expecterd # True
isUpperLower("ABC")

# "abc" expecterd # True
isUpperLower("abc")

# "ABC" expecterd # True
isUpperLower("Abc")


# test Upper and Lower # re.fullmatch(r'[A-Z]{5,10}', text)
def isLen(text:str) -> None:

    print(True if re.fullmatch(r'[A-Za-z]{5,10}', text) else False)

# "ABC" expecterd # False -> len == 3
isLen("ABC")

# "abcdef" expecterd # True -> len == 6
isLen("abcdef")

# "aAaAaAaAaAa" expecterd # False -> len == 11
isLen("aAaAaAaAaAa")