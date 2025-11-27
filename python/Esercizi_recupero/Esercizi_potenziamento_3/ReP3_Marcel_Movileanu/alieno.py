'''
Alieno (che eredita da Creatura) con le seguenti proprietà:
- attributi: matricola (di tipo intero positivo), munizioni (una lista di 15 interi positivi)
- metodi: setter, getter, __str__
In particolare:

    il metodo setMatricola() (privato), non riceve argomenti in input e deve inizializzare l'attributo matricola con un numero intero positivo casuale tra 10000 e 90000.

Per generare un numero intero casuale nell'intervallo [a, b] (ovvero estremi inclusi), importare il modulo random e usare la funzione randint(a,b) del modulo;
 

    il metodo setMunizioni() (privato) non riceve argomenti in input e deve inizializzare l'attributo munizioni con una lista di 15 numeri interi positivi i cui elementi sono numeri della sequenza 0, 1, 4, 9, 16, 25, 36, 49, ... Usare le list comprehension.

    il metodo __init__ deve inizializzare la superclasse, inizializzare la matricola e le munizioni.

Inoltre, i nomi di tutti gli alieni devono essere "Robot-" + matricola (ad esempio, "Robot-16326", scritto con la R maiuscola).
Pertanto, nel metodo __init__ impostare il nome dell'Alieno come richiesto, effettuando opportuni controlli. Nel caso in cui il nome dell'alieno non sia conforme, mostrare il seguente messaggio e re-impostare il nome in modo corretto: "Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!".

    il metodo __str__ deve mostrare in output: "Alieno: nome alieno" (ad esempio: Alieno: Robot-16326)
'''


from creatura import Creatura
from random import randint

class Alieno(Creatura): 

    _matricola: int # Intero >= 0
    _munizioni: list[int]

    def __init__(self, nome: str):
        super().__init__(nome)
        self._setMatricola()
        self._setMunizioni()
        if self._nome != 'Robot' or not(10000 <= self.matricola() <= 90000):
            print('Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! '
                  'Reimpostazione nome Alieno in Corso!')
            self._nome = f'Robot-{self.matricola()}'
        else:
            self._nome = nome.title() + f'-{self.matricola()}'

    def _setMatricola(self) -> None:
        self._matricola = randint(10000, 90000)

    def _setMunizioni(self) -> None:
        self._munizioni = [n**2 for n in range(15)]

    def matricola(self) -> int:
        return self._matricola
    
    def munizioni(self) -> list[int]:
        return self._munizioni
    
    def __str__(self):
        return super().__str__()



if __name__ == '__main__':

    al1: Alieno = Alieno(nome='Bob')

    print(al1.nome())
    print(isinstance(al1, Alieno))