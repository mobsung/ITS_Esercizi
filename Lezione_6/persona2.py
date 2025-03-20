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
    def setAge(self, age:int) -> int:

        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

#funzione che mi consenta di ritornare il valore di self.name
    def getName(self) -> str:
        return self.name
    
#funzione che mi consenta di ritornare il valore di self.lastname
    def getLastName(self) -> str:
        return self.lastname

#funzione che mi consenta di ritornare il valore di self.age
    def getAge(self) -> int:
        return self.age


