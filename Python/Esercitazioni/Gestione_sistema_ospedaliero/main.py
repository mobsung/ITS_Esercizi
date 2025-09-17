'''
Scrivere, infine, il codice driver che gestisca due dottori e due liste di pazienti. La prima lista di pazienti deve contenere 3 pazienti, mentre la seconda 1 solo paziente.

    Impostare l'età di ogni medico, affinché i due medici risultino validi!
    Il primo medico e il secondo medico si presentano, richiamando il rispettivo metodo doctorGreet().
    Creare un oggetto fattura chiamato fattura1. Alla fattura 1 devono essere associati il dottore_1 e la lista di 3 pazienti.
    Creare un oggetto fattura chiamato fattura2. Alla fattura 2 devono essere associati il dottore_2 e la lista di un solo paziente.
    Stampare in output il salario di ogni singolo dottore. Ad esempio:

      "Salario Dottore1: ... euro!
       Salario Dottore2: ... euro!"

    Rimuovere un paziente dalla lista dei pazienti del dottore 1 ed inserire tale paziente nella lista del dottore 2.
    Stampare in output il salario di ogni dottore.
    Stampare in output il guadagno totale incassato dall'ospedale. Il guadagno totale viene calcolato sommando i guadagni di ogni dottore. Esempio:

"In totale, l'ospedale ha incassato: tot euro!"
'''
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura


doctor1: Dottore = Dottore(first_name='Gino', last_name='Il Dottore', specialization='Pediatra', parcel=10.5)
doctor2: Dottore = Dottore(first_name='Gina', last_name='La Dottoressa', specialization='Cardiologa', parcel=12.0)


patient1: Paziente = Paziente(first_name='Lanto', last_name='Leandro', codice='#1')
patient2: Paziente = Paziente(first_name='Lorenzo', last_name='Anzivino', codice='#2')
patient3: Paziente = Paziente(first_name='Cristiano', last_name='Coccia', codice='#3')
patient4: Paziente = Paziente(first_name='Stefano', last_name='Reali', codice='#4')

# patient5: Paziente = Paziente(first_name='Giulia', last_name='Bianchi', codice='#5')
# patient6: Paziente = Paziente(first_name='Marco', last_name='Verdi', codice='#6')
# patient7: Paziente = Paziente(first_name='Alessandro', last_name='Neri', codice='#7')
# patient8: Paziente = Paziente(first_name='Francesca', last_name='Gallo', codice='#8')

doctor1.setAge(40)
doctor2.setAge(31)

print('--> I dottori si presentano')
doctor1.doctorGreet()
doctor2.doctorGreet()

print('-' * 100)

print('--> Creazione oggetti Fattura')
fattura1: Fattura = Fattura(patients=[patient1, patient2, patient3], doctor=doctor1)
fattura2: Fattura = Fattura(patients=[patient4], doctor=doctor2)

print('-' * 100)

print('--> Salario dottiri senza modifiche')
print(f'Salario {doctor1.getName()} {doctor1.getLastname()}: {fattura1.getSalary()}')
print(f'Salario {doctor2.getName()} {doctor2.getLastname()}: {fattura2.getSalary()}')

print('-' * 100)

print('--> Salario dottori dopo modifiche')

fattura1.removePatient('#1')
fattura2.addPatient(patient1)

print(f'Salario {doctor1.getName()} {doctor1.getLastname()}: {fattura1.getSalary()}')
print(f'Salario {doctor2.getName()} {doctor2.getLastname()}: {fattura2.getSalary()}')


print('-' * 100)

print('--> Incasso Ospedale')

print(f"In totale, l'ospedale ha incassato: tot {fattura1.getSalary() + fattura2.getSalary()} euro!")

