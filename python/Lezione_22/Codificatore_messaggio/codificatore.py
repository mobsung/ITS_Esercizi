'''
Si crei una classe astratta chiamata CodificatoreMessaggio che ha un solo metodo astratto codifica(testoInChiaro), dove testoInChiaro sarà il messaggio da codificare. Il metodo restituirà il messaggio codificato.

Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo decodifica(testoCodificato), dove testoCodificato sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.

Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato chiave. Si definisca il metodo codifica(testoInChiaro) così che ogni lettera del testo sia spostata dal valore contenuto in chiave.
Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e', la lettera 'c' sarà sostituita da 'f' e così via.

     Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).


Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato n. Si definisca il metodo codifica(testoInChiaro) così che il messaggio sia combinato n volte. Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna delle metà in modo alternato. Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi' (nel caso in cui la lunghezza del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà). Il messaggio combinato è 'afbgchdie'.

    Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e ritorni il testo cifrato da usare nel metodo codifica(testoInChiaro).


Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

    Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che compie un'azione inversa al metodo sposta_carattere().

    Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che compie un'azione inversa al metodo combinazione().


Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.
'''

from abc import ABC, abstractmethod
from string import ascii_lowercase

class CodificatoreMessaggio:

    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass


class DecodificatoreMessaggio:

    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        pass


class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int) -> None:
        self.chiave = chiave

    def codifica(self, testoInChiaro: str) -> str:
        alpha: str = ascii_lowercase
        crypted_word: str = ''

        for char in testoInChiaro:
            if char.isalpha():
                
                upp: bool = True if char.isupper() else False

                for index, letter in enumerate(alpha):
                    if char.lower() == letter:
                        pos: int = (index + self.chiave) % len(alpha)

                crypted_word += alpha[pos].upper() if upp == True else alpha[pos]

            else:
                crypted_word += char

        return crypted_word
    

    def decodifica(self, testoCodificato: str) -> str:
        alpha: str = ascii_lowercase
        decrypted_word: str = ''

        for char in testoCodificato:
            if char.isalpha():

                upp: bool = True if char.isupper() else False

                for index, letter in enumerate(alpha):
                    if char.lower() == letter:
                        pos: int = index - (self.chiave % len(alpha))
                
                decrypted_word += alpha[pos].upper() if upp == True else alpha[pos]

            else:
                decrypted_word += char

        return decrypted_word
    
    def scrivi_su_file(self, nome_file: str, testo: str) -> None:
        with open(nome_file, "w", encoding="utf-8") as file:
            file.write(testo)
    
    def leggi_da_file(self, nome_file: str) -> str:
        with open(nome_file, "r", encoding="utf-8") as file:
            return file.read()


class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, n: int) -> None:
        self.n = n

    def codifica(self, testoInChiaro: str) -> str:
        j: int = 0
        result: str = testoInChiaro

        while self.n > j:

            if len(testoInChiaro) % 2 == 0:
                first: str = result[:len(result) // 2]
                second: str = result[(len(result) - len(first)):]
            else:
                first = result[:(len(result) // 2) + 1]
                second: str = result[(len(result) - len(first)) + 1:]

            result = ''

            for i in range(len(second)):
                result += first[i]
                result += second[i]

            if len(testoInChiaro) % 2 != 0:
                result += first[-1]

            j += 1
        return result


    def decodifica(self, testoCodificato: str):
        j: int = 0
        result: str = testoCodificato

        while self.n > j:

            first: str = f"{''.join([result[ind] for ind in range(len(result)) if ind % 2 == 0])}"
            second: str = f"{''.join([result[ind] for ind in range(len(result)) if ind % 2 != 0])}"

            result = first + second

            j += 1

        return result
    

    def scrivi_su_file(self, nome_file: str, testo: str) -> None:
        with open(nome_file, "w", encoding="utf-8") as f:
            f.write(testo)

    def leggi_da_file(self, nome_file: str) -> str:
        with open(nome_file, "r", encoding="utf-8") as f:
            return f.read()
        



def test_cifratore_a_scorrimento():
    print("Test del Cifratore a Scorrimento:")

    cifratore = CifratoreAScorrimento(chiave=3)

    # 1) Creiamo un file di input con testo in chiaro (solo la prima volta)
    testo_iniziale = "aaabbb"
    cifratore.scrivi_su_file("./Python/Lezione_22/Codificatore_messaggio/input.txt", testo_iniziale)

    # 2) Lettura del testo da file
    testo_in_chiaro = cifratore.leggi_da_file("input.txt")

    # 3) Codifica
    testo_codificato = cifratore.codifica(testo_in_chiaro)

    # 4) Scrittura testo codificato su file
    cifratore.scrivi_su_file("./Python/Lezione_22/Codificatore_messaggio/scorrimento.txt", testo_codificato)

    # 5) Stampa testo codificato
    print("Testo codificato:")
    print(testo_codificato)

    # 6) Decodifica
    testo_decodificato = cifratore.decodifica(testo_codificato)

    # 7) Stampa testo decodificato
    print("Testo decodificato:")
    print(testo_decodificato)


def test_cifratore_a_combinazione():
    print("\nTest del Cifratore a Combinazione:")

    cifratore = CifratoreACombinazione(n=3)

    # 1) Creiamo un file di input con testo in chiaro (solo la prima volta)
    testo_iniziale = "aaabbb"
    cifratore.scrivi_su_file("input.txt", testo_iniziale)

    # 2) Lettura del testo da file
    testo_in_chiaro = cifratore.leggi_da_file("input.txt")

    # 3) Codifica
    testo_codificato = cifratore.codifica(testo_in_chiaro)

    # 4) Scrittura testo codificato su file
    cifratore.scrivi_su_file("./Python/Lezione_22/Codificatore_messaggio/combinazione.txt", testo_codificato)

    # 5) Stampa testo codificato
    print("Testo codificato:")
    print(testo_codificato)

    # 6) Decodifica
    testo_decodificato = cifratore.decodifica(testo_codificato)

    # 7) Stampa testo decodificato
    print("Testo decodificato:")
    print(testo_decodificato)


if __name__ == "__main__":
    test_cifratore_a_scorrimento()
    test_cifratore_a_combinazione()
