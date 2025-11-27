'''
Creare un file chiamato "paziente.py".
In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
- Definire i seguenti metodi:

    - costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.

    - setIdCode(idCode): consente di impostare il codice identificativo del paziente.

    - getidCode(): consente di ritornare il codice identificativo del paziente.

    - patientInfo(): stampa in output le informazioni del paziente in questo modo:

        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"
'''

from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str, codice: str) -> None:
        super().__init__(first_name, last_name)
        self.setIdCode(codice)

    def setIdCode(self, idCode) -> None:

        if idCode and type(idCode) == str:
            self.__idCode = idCode
        else:
            self.__idCode = None
            print('Il codice inserito non è una stringa!')

    def getidCode(self) -> str:

        return self.__idCode
    
    def patientInfo(self) -> None:

        print(f'Paziente: {self.getName()} {self.getLastname()} ID: {self.getidCode()}')
