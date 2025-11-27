'''
Frequenza di Parole Uniche con Normalizzazione
Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.
Requisiti:
● Suddividi l’input sugli spazi bianchi per ottenere i token.
● Normalizza ogni token:
1. Converti in minuscolo.
2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip()
con un insieme di caratteri di punteggiatura).
● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della
punteggiatura.
● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi
interi.
Esempio:
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}
'''
import string

def count_normalize(stringa: str) -> dict[str, int]:

    imp_list: list[str] = stringa.split()
    normalized_list: list[str] = [word.strip(string.punctuation).lower() for word in imp_list]
    out_dict: dict[str, int] = {}

    for word in normalized_list:
        if word not in out_dict:
            out_dict[word] = 1
        else:
            out_dict[word] += 1

    return out_dict




if __name__ == '__main__':

    print(count_normalize("Hello, world! Hello... PYTHON? world."))
     