'''
Hai una lista di parole parole = ["cane", "gatto", "elefante", "ratto", "orso"] Estrai solo le parole con più di 4 lettere usando filter() e lambda.
'''

parole = ["cane", "gatto", "elefante", "ratto", "orso"]

print(list(filter(lambda x: len(x) > 4, parole)))