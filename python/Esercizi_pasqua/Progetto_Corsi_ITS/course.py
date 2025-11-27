'''
La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
- Metodi:
    - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
    - get_groups(): Restituisce la lista dei gruppi nel corso.
    - add_group(group): Aggiunge un gruppo al corso.
'''

from group import *
from building import *


class Course():

    # Dizionario per verificare che lo stesso oggetto di tipo Student non sia stato gia inserito nello stesso oggetto di tipo Group
    asigned_students: dict[Student, Group] = {}

    def __init__(self, name: str):

        self.setName(name)
        self.groups: list[Group] = [] # Lista che salva tutti gli oggetti creati di tipo Group
        
    
    # Metodo che consente di impostare il nome degli oggetti di tipo Group
    def setName(self, name: str) -> None:

        self.name = name


    # Metodo che registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti
    def register(self, student:Student) -> None:  

        for group in self.groups:

            if student not in self.asigned_students:
                if len(group) < group.get_limit():
                    self.asigned_students[student] = group
                    group.add_student(student)
                    return True
            
            # Verifica se l'oggetto di tipo Student è stato già inserito nell'oggetto di tipo Group
            elif self.asigned_students.get(student) == group:
                return False
            
            # Verifica se l'oggetto di tipo Student è stato già inserito in un altro oggetto di tipo Group
            else:
                return False
                
    # Metodo che eestituisce la lista dei gruppi nel corso
    def get_groups(self) -> list[Group]:

        return self.groups

    #Metodo che consente di aggiungere un gruppo al corso
    def add_group(self, group:Group):

        self.groups.append(group)




if __name__ == "__main__":

    # Creazione degli edifici
    smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=(-2, 3))
    armellini = Building(name="ITIS", address="Basilica San Paolo", floors=(0, 4))

    # Aggiunta delle stanze all'edificio smi
    smi.add_room(Room(id="123", floor=3, seats=32))
    smi.add_room(Room(id="333", floor=0, seats=42))
    smi.add_room(Room(id="111", floor=6, seats=32))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
    smi.add_room(Room(id="111", floor=-1, seats=32))

    # Aggiunta delle stanze all'edificio smi
    armellini.add_room(Room(id="567", floor=3, seats=22))
    armellini.add_room(Room(id="888", floor=0, seats=32))
    armellini.add_room(Room(id="999", floor=6, seats=22))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
    armellini.add_room(Room(id="999", floor=2, seats=22))

    # Output dei risultati
    print("### SMI ###")
    print(f"Stanze nell'edificio SMI: {[room.get_id() for room in smi.get_rooms()]}")
    print(f"Area totale dell'edificio SMI: {smi.area()} m²")
    print("### ARMELLINI ###")
    print(f"Stanze nell'edificio ITIS: {[room.get_id() for room in armellini.get_rooms()]}")
    print(f"Area totale dell'edificio ITIS: {armellini.area()} m²")


    # Creazione dei gruppi
    fullstack = Group(name="Fullstack", limit=1)
    cloud = Group(name="Cloud", limit=10)
    cyber = Group(name="Cyber", limit=10)

    # Creazione di un corso e aggiunta dei gruppi al corso
    course = Course(name="Python")
    course.add_group(fullstack)
    course.add_group(cloud)
    course.add_group(cyber)


    # Registrazione degli studenti al corso
    course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
    course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))
    course.register(Student(cf="9101", name="Luca", surname="Bianchi", age=25))
    course.register(Student(cf="2345", name="Marco", surname="Rossi", age=32))
    course.register(Student(cf="6789", name="Paolo", surname="Verdi", age=38))
    course.register(Student(cf="1011", name="Giulia", surname="Neri", age=21))
    course.register(Student(cf="3456", name="Anna", surname="Gialli", age=27))
    course.register(Student(cf="7890", name="Maria", surname="Blu", age=35))
    course.register(Student(cf="1112", name="Sara", surname="Viola", age=23))
    course.register(Student(cf="4567", name="Giovanni", surname="Arancione", age=31))
    course.register(Student(cf="8901", name="Andrea", surname="Rosa", age=24))
    course.register(Student(cf="1123", name="Matteo", surname="Marrone", age=30))
    course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))

    print("### COURSE DETAILS ###")
    print(f"Studenti nel gruppo Fullstack: {[student.cf for student in fullstack.get_students()]}")
    print(f"Studenti nel gruppo Cloud: {[student.cf for student in cloud.get_students()]}")
    print(f"Studenti nel gruppo Cyber: {[student.cf for student in cyber.get_students()]}")