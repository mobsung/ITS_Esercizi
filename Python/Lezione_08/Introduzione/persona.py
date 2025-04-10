


class Persona():

    def __init__(self, name:str = "", last_name:str = "", age:int = 0):

        self.setName(name)
        self.setLastName(last_name)
        self.setAge(age)


    def setName(self, name:str) -> None:

        self.name = name

    
    def setLastName(self, last_name:str) -> None:

        self.last_name = last_name


    def setAge(self, age:int) -> None:

        self.age = age

        if age < 0:
            print("The age has to be a positive number - it will be set to 0!")
            self.age = 0

        elif age > 130:
            print("The age is to high! - it will be set to 130!")
            self.age = 130

    
    def getName(self) -> str:

        return self.name
    

    def getLastName(self) -> str:

        return self.last_name
    

    def getAge(self) -> int:

        return int(self.age)
    

    def __str__(self) -> str:
        
        return f'Name: {self.name}\nLast name: {self.last_name}\nAge: {self.age}\n{20 * "-"}'
    

    def __call__(self) -> None:
        
        if self.age < 18:
            print(f"{self.name} {self.last_name} e' minorenne!")
        elif 18 <= self.age < 30:
            print(f"{self.name} {self.last_name} e' maggiorenne!")
        elif 30<= self.age < 80:
            print(f"{self.name} {self.last_name} e' una persona adulta!")
        else:
            print(f"{self.name} {self.last_name} e' una persona anziana!")
        


if __name__ == "__main__":

    marcel:Persona = Persona()

    print(marcel)

    marcel.setName("Marcel")
    marcel.setLastName("Movileanu")
    marcel.setAge(24)

    print(marcel)

    marcel()