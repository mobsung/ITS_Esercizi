'''
Le classi Student e Lecturer ereditano da Person.
Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
    - set_group(group): Associa un gruppo di studio allo studente
'''

from person import Person

class Lecturer(Person):

    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)