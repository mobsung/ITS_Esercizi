

class Student:


    def __init__(self, name:str, studyProgram:str, age:int, gender:str):


        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender


    def print_info(self):


        print(f'Name: {self.name} - Study program: {self.studyProgram} - Age: {self.age} - Gender: {self.gender}')

    

marcel: Student = Student("Marcel", "Python", 24, "Male")
stefano: Student = Student("Stefano", "Python", 34, "Male")
leandro: Student = Student("Leandro", "Python", 27, "Male")
francesco: Student = Student("Francesco", "Python", 12, "Male")


marcel.print_info()
stefano.print_info()
leandro.print_info()
francesco.print_info()


    