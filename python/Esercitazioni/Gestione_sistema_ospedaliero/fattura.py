'''
Creare un file chiamato "fatture.py".
In tale file, creare una classe chiamata Fattura.

- Definire i seguenti metodi:

    - init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
    
    - getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.

    - getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.

    - addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"

    - removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
'''

from dottore import Dottore
from paziente import Paziente

class Fattura:

    def __init__(self, patients: list[Paziente], doctor: Dottore) -> None:
        
        if doctor.isAValidDoctor():
            self.__patients = patients
            self.__doctor = doctor
            self.__fatture: int = len(patients)
            self.__salary: int = 0
        
        else:
            self.__patients = None
            self.__doctor = None
            self.__fatture = None
            self.__salary = None
            print('Non è possibile creare la classe fattura poichè il dottore non è valido!')

    def getSalary(self) -> int | None:

        self.__salary = self.__doctor.getParcel() * self.__fatture
        return self.__salary
    
    def getFatture(self) -> int | None:

        self.__fatture: int = len(self.__patients)
        return self.__fatture
    
    def addPatient(self, newPatient: Paziente) -> None:

        self.__patients.append(newPatient)
        self.getSalary()
        self.getFatture()

    def removePatient(self, idCode) -> None:

        for patient in self.__patients:
            if patient.getidCode() == idCode:
                self.__patients.remove(patient)
                self.getSalary()
                self.getFatture()
                print(f'Alla lista del Dottor {self.__doctor.getName()} è stato rimosso il paziente {patient.getidCode()}')
                return
        


if __name__ == '__main__':

    doctor1: Dottore = Dottore(first_name='Gino', last_name='Il Dottore', specialization='Pediatra', parcel=10.5)

    patient1: Paziente = Paziente(first_name='Lanto', last_name='Leandro', codice='#1')
    patient2: Paziente = Paziente(first_name='Lorenzo', last_name='Anzivino', codice='#2')
    patient3: Paziente = Paziente(first_name='Cristiano', last_name='Coccia', codice='#3')
    patient4: Paziente = Paziente(first_name='Stefano', last_name='Reali', codice='#4')

    doctor1.setAge(40)

    fattura1: Fattura = Fattura(patients=[patient1, patient2, patient3, patient4], doctor=doctor1)

    patient1.setAge(20)
    patient2.setAge(15)
    patient3.setAge(32)
    patient4.setAge(14)

    fattura1.removePatient(idCode='#1')
    print(fattura1.getSalary())

    fattura1.addPatient(newPatient=patient1)

    print(fattura1.getFatture())
    print(fattura1.getSalary())

