'''
La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
'''

class Person():

    

    def __init__(self, cf:str, name:str, surname:str, age:int):

        self.setCf(cf)
        self.setName(name)
        self.setLastName(surname)
        self.setAge(age)


    # Metodo che consente di impostare il Cf per gli oggetti di tipo Person
    def setCf(self, cf:str) -> None:

            self.cf = cf
            


    # Metodo che consente di impostare il nome per gli oggetti di tipo Person
    def setName(self, name:str) -> None:

        self.name = name


    # Metodo che consente di impostare il cognome per gli oggetti di tipo Person
    def setLastName(self, surname:str) -> None:

        self.surname = surname


    # Metodo che consente di impostare l'età per gli oggetti di tipo Person
    def setAge(self, age:int) -> None:

        self.age = age

        if age < 0:
            print("The age has to be a positive number - it will be set to 0!")
            self.age = 0

        elif age > 130:
            print("The age is to high! - it will be set to 130!")
            self.age = 130

    
    # Metodo che restituisce il nome per gli oggetti di tipo Person
    def getName(self) -> str:

        return self.name


    # Metodo che restituisce il Cf per gli oggetti di tipo Person
    def getCf(self) -> str:

        return self.cf


    # Metodo che restituisce il Cognome per gli oggetti di tipo Person
    def getLastName(self) -> str:

        return self.surname


    # Metodo che restituisce l'età per gli oggetti di tipo Person
    def getAge(self) -> int:

        return self.age
    
        

if __name__ == "__main__":
     
    person1 = Person(cf="CF123", name="John", surname="Doe", age=30)
    person2 = Person(cf="CF123", name="John", surname="Doe", age=30)

    a = []

    a.append(person1)

    print(person2 in a)
