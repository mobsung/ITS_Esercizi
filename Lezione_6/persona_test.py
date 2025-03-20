'''#dal file persona.py imnporta la classe Persona
from persona import Persona

#crea una persona
mm:Persona = Persona("Marcel", "Movileanu", 24)

print(mm)

print(mm.name, mm.lastname, mm.age)

#richiamare la funzione displayData della classe Persona per mostrare i dati relativi alla persona 

mm.displayData()

print("--------------------")'''

from persona2 import Persona

mm:Persona = Persona()

mm.displayData()
print("--------------------")

mm.setName("Marcel")
mm.displayData()
print("--------------------")

mm.setLastName("Movileanu")
mm.displayData()
print("--------------------")

mm.setAge(24)
mm.displayData()
print("--------------------")

