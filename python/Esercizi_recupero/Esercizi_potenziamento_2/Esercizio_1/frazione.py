'''


8.A Si Scriva in Python in un file frazioni.py una classe Frazione, i cui attributi privati siano rispettivamente numeratore e denominatore.
Si definiscano i metodi __init__, setter, getter, __str__, value.
In particolare:

    il metodo value(), deve restituire il valore della frazione, ovvero numeratore / denominatore arrotondato a 3 cifre decimali;

    il metodo __str__ deve mostare in output la frazione nel seguente modo: "numeratore / denominatore ";
    i metodi setter devono controllare che il valore inserito sia un intero, in caso contrario il numeratore ed il denominatore devono essere impostati per default rispettivamente a 13 e 5. Inoltre, il metodo setter relativo al denominatore deve assicurarsi che questo non sia mai uguale a 0. Nel caso in cui il denominatore passato sia 0, impostarlo per default a 5.

Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la funzione is_integer().

Scrivere nel file frazione.py una funzione  mcd(int x, int y) per il calcolo del Massimo Comune Divisore.
 
Nel caso in cui esista un Massimo Comun Divisore tra i numeri x e y, allora la funzione deve ritornarlo come numero intero.
Altrimenti, nel caso in cui non esista un massimo Comun Divisore tra i numeri x e y, la funzione deve ritornare 1.
   

Suggerimento: per semplicità, per implementare la funzione richiesta, trovare una soluzione che generalizzi l'esempio proposto e che tenga conto dei casi x > y e x < y per evitare di replicare righe di codice.
   

8.C Una frazione si dice irriducibile se il numeratore e il denominatore non hanno divisori comuni, ovvero il più grande divisore comune tra numeratore e denominatore è 1.

Sia l una lista di frazioni, ovvero una lista di oggetti della classe Frazione.

Si scriva nel file frazioni.py una funzione chiamata semplifica() che data in input una lista di frazioni ritorni in output una lista di frazioni irriducibili.
 
Nello specifico:

    se una frazione f della lista data in input è già irriducibile, allora inserire questa frazione f nella lista da ritornare in output.

 

    se una frazione f della lista data in input può essere semplificata, in una frazione irriducibile f1, allora si deve prima semplicare la frazione f, ottenendo la frazione irriducibile f1 e poi inserire f1 nella lista da ritornare in output.


Suggerimento: Leggere bene la traccia dell'intero esercizio per capire come implementare la funzione semplifica.
Inserire in modo adeguato le seguenti frazioni nella lista l.
'''

from typing import Self

class Frazione:

    __numeratore: int
    __denominatore: int

    def __init__(self, numeratore: int, denominatore: int) -> None:
        self.setNumeratore(numeratore)
        self.setDenominatore(denominatore)

    def numeratore(self) -> int:
        return self.__numeratore
    
    def denominatore(self) -> int:
        return self.__denominatore

    def setNumeratore(self, numeratore: int) -> None:
        if type(numeratore) != int or numeratore == 0:
            self.__numeratore = 13
        
        else:
            self.__numeratore = numeratore

    def setDenominatore(self, denominatore: int) -> None:
        if type(denominatore) != int or denominatore == 0:
            self.__denominatore = 5
        
        else:
            self.__denominatore = denominatore

    def value(self) -> float:
        return round(self.numeratore() / self.denominatore(), 3)
    
    def __str__(self) -> str:
        return f'{self.numeratore()}/{self.denominatore()}'
    
    def __repr__(self):
        return f'{self.numeratore()}/{self.denominatore()}'

    def mdc(self, x: int, y: int) -> int:
        comun_divisore: int = 1

        i: int = 2
        min = x if x < y else y
    
        while min >= i:
            if x % i == 0 and y % i == 0:
                comun_divisore = i
            i += 1

        return comun_divisore        
    
    def semplifica(self, lista: list[Self]) -> list[Self]:

        result_list: list[Self] = []

        for frazione in lista:
            if self.mdc(frazione.numeratore(), frazione.denominatore()) == 1:
                result_list.append(frazione)
            else:
                maxdc: int = self.mdc(frazione.numeratore(), frazione.denominatore())
                result_list.append(Frazione(frazione.numeratore() / maxdc, frazione.denominatore() / maxdc))

        return result_list
    
    def compare(self, lista_originale: list[Self], lista_semplificata: list[Self]) -> str:
        pass



if __name__ == '__main__':

    f1: Frazione = Frazione(2, 4)
    print(f1.numeratore())
    print(f1.denominatore())
    print(f1.value())
    print(f1)

    print(f1.mdc(18, 12))

    print(f1.semplifica([Frazione(1, 1), Frazione(12, 18), Frazione(5, 7), Frazione(2, 8)]))