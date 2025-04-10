from studente import *

#creare un oggetto p della classe Persona
p:Persona = Persona("Marcel", "Movileanu", 24)

#visualizzare le informazioni relative alla persona p
print(p)

#creare un oggetto studente1 della classe Studente
studente1:Studente = Studente("Stefano", "Reali", 34, "0123456")

#visualizzare le informazioni relative al studente1
print(studente1)

#voglio controllare se studente1 sia istanza della clase Studente
if isinstance(studente1, Studente):
    print(f'L\'oggetto studente1 è un oggetto della classe Studente\n{20 * "-"}')

#voglio sapere se studene1 sia anche istanza della classe persona dato che studente eredita dalla classe Persona
if isinstance(studente1, Persona):
    print(f'L\'oggetto: studente1 è istanza della classe Persona e della classe Studente\n{20 * "-"}')
else:
    print(f'L\'oggetto: studente1 è istanza della classe Studente ma non della classe Persona\n{20 * "-"}')

#voglio controllare se Studente è una sottoclasse della classe Persona
if issubclass(Studente, Persona):
    print(f'La classe Studente è sotto classe della classe Persona\n{20 * "-"}')

studente1()

studente1.getMediaEsami([8, 9, 10])

studente2:Studente = Studente(p.getName(), p.getLastName(), p.getAge(), "0987654")

print(studente2)

print(f'{studente1 == studente1}\n{20 * "-"}')