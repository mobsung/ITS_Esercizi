'''
La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), una lista di studenti (students) e una lista di docenti (lecturers).
- Metodi:
    - get_name(): Restituisce il nome del gruppo
    - get_limit(): Restituisce il limite di studenti nel gruppo
    - get_students(): Resituisce la lista di studenti nel gruppo
    - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti. Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
    - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
    - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.
'''


from student import Student
from lecturer import Lecturer

class Group():

    def __init__(self, name:str, limit:int):
        
        self.setName(name)
        self.setLimit(limit)
        self.students = [] # Lista che tiene conto degli oggetti creati di tipo Student
        self.lecturers = [] # Lista che tiene conto degli oggetti creati di tipo Lecturer


    # Metodo che consente di impostare il nome degli oggetti di tipo Group
    def setName(self, name:str) -> None:

        self.name = name


    # Metodo che consente di impostare il limite di oggetti di tipo Student negli oggetti di tipo Group
    def setLimit(self, limit:int) -> None:

        self.limit = limit


    # Metodo che restituisce il nome del gruppo
    def get_name(self) -> str:

        return self.name
    

    # Metodo che restituisce il limite di studenti nel gruppo
    def get_limit(self) -> int:

        return self.limit
    

    # Metodo che resituisce la lista di studenti nel gruppo
    def get_students(self) -> list:

        return self.students
    

    # Metodo che restituisce il limite di docenti nel gruppo
    def get_limit_lecturers(self) -> list:

        return self.lecturers
    

    def __str__(self):
        
        return f'{self.name}'

    # Metodo che aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto
    def add_student(self, student:Student):

        if len(self.students) < self.limit:
            if len(self.lecturers) == 0 and len(self.students) <= 10:
               self.students.append(student)
               return True
            else:
                if len(self.students) / len(self.lecturers) < 10:
                    self.students.append(student)
                    return True
        return False

    # Metodo che aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto
    def add_lecturer(self, lecturer:Lecturer):

        if len(self.lecturers) == 0:
            self.lecturers.append(lecturer)
        else:
            if round(len(self.students) / 10, 0) <= len(self.lecturers):
                print("There aren't enough Students.")

            else:
                self.lecturers.append(lecturer)

    
    def __len__(self):

        return len(self.students)
    


if __name__ == "__main__":

    student1 = Student(cf="CF456", name="Jane", surname="Smith", age=20)

    # Test metodo set_group della classe Student
    group1 = Group(name="Group A", limit=10)
    student1.set_group(group1)
    print("\nDopo set_group di student1:")
    print(f"Gruppo di student1: {student1.group.get_name()}, Atteso: Group A")
