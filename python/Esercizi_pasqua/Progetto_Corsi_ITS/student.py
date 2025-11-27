'''
Le classi Student e Lecturer ereditano da Person.
Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
    - set_group(group): Associa un gruppo di studio allo studente
'''

from person import Person

class Student(Person):

    def __init__(self, cf, name, surname, age, group = None):
        super().__init__(cf, name, surname, age)

        self.set_group(group)


    # Metodo che associa un gruppo di studio allo studente
    def set_group(self, group) -> None:

        self.group = group


    def __str__(self):
        
        return f'{self.cf} - {self.surname}'



if __name__ == "__main__":

    student1 = Student(cf="CF456", name="Jane", surname="Smith", age=20)