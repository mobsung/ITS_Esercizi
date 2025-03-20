class Persona:

    def __init__(self):
        
        self.name = ""
        self.lastname = ""
        self.age = 0

#funzione che mi conseta di mostrare in output i dati della classe Persona
    def displayData(self) -> None:

        print(f'Name: {self.name}\nLast name: {self.lastname}\nAge: {self.age}')


#funzione che mi conseta di impostare il valore di self.name
    def setName(self, name:str) -> None:

        self.name = name
    
#funzione che mi conseta di impostare il valore di self.lastname
    def setLastName(self, lastname:str) -> None:

        self.lastname = lastname

#funzione che mi conseta di impostare il valore di self.lastname
    def setAge(self, age:int) -> None:

        self.age = age


