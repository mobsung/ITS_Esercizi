from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @abstractmethod
    def get_role(self) -> None:
        pass

    def __str__(self) -> str:
        return f'Name: {self._name} - Age: {self._age}'
    

class Student(Person):

    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self._student_id = student_id
        self._courses: list[Course] = []

    def get_role(self) -> str:
        return 'Student'
    
    def enroll(self, course: 'Course') -> None:
        if course not in self._courses:
            self._courses.append(course)
            if self not in course._students:
                course.add_student(self)
        else:
            print(f'Lo studente {self._name} è già iscritto al corso {course}')

    def __str__(self) -> str:
        return super().__str__() + f' - ID: {self._student_id} - Role: {self.get_role()}'


class Professor(Person):

    def __init__(self, name: str, age: int, professor_id: str, department: 'Department' = None):
        super().__init__(name, age)
        self._professor_id = professor_id
        self._courses: list[Course] = []
        self.department = None
        if department:
            self.setDepartment(department)

    def get_role(self) -> str:
        return 'Professor'
    
    def assign_to_course(self, course: 'Course') -> None:
        if course not in self._courses:
            course.set_professor(self)
            self._courses.append(course)

    def setDepartment(self, department: 'Department') -> None:
        if self.department != department:
            self.department = department
            if self not in department.professors:
                department.add_professor(self)

    def __str__(self) -> str:
        return super().__str__() + f' - ID: {self._professor_id} - Department: {self.department.getDepartment()}'


class Course:

    def __init__(self, course_name: str, course_code: str):
        self._course_name = course_name
        self._course_code = course_code
        self._professor: Professor = ''
        self._students: list[Student] = []

    def add_student(self, student: Student) -> None:
        if student not in self._students:
            self._students.append(student)
            if self not in student._courses:
                student.enroll(self)

    def set_professor(self, professor: Professor) -> None:
        self._professor = professor

    def __str__(self) -> str:
        student_str = '\n'.join(str(student) for student in self._students)
        return f'Course name: {self._course_name} - Course Code: {self._course_code} - Course instructor: {self._professor}\n--> Student list\n{student_str}\n'
                  

class Department:

    def __init__(self, department_name: str):
        self._department_name = department_name
        self._courses: list[Course] = []
        self.professors: list[Professor] = []

    def add_course(self, course: Course) -> None:
        if course not in self._courses:
            self._courses.append(course)

    def add_professor(self, professor: Professor) -> None:
        if professor not in self.professors:
            self.professors.append(professor)
            if professor.department != self:
                professor.setDepartment(self)
    
    def getDepartment(self) -> str:
        return self._department_name

    def __str__(self):
        professors_str: str = '\n'.join(str(professor) for professor in self.professors)
        courses_str: str = '\n'.join(str(course) for course in self._courses)
        return f'Department name: {self._department_name}\n--> Professors list in Department: \n{professors_str}\n--> Courses list in Department: \n{courses_str}\n'
    

class University: 

    def __init__(self):
        self._departments: list[Department] = []
        self._students: list[Student] = []

    def add_department(self, department: Department) -> None:
        if department not in self._departments:
            self._departments.append(department)

    def add_student(self, student: Student) -> None:
        if student not in self._students:
            self._students.append(student)

    def __str__(self) -> str:
        departments_str: str = '\n'.join(str(department) for department in self._departments)
        students_str: str = '\n'.join(str(student) for student in self._students)
        return f'--> DEPARTMENTS <--\n{departments_str}--> STUDENTS <--\n{students_str}'



if __name__ == '__main__':

    # Courses objects
    python_course = Course(course_name='Python', course_code='#0001')
    ai_course = Course(course_name='Artificial Intelligence', course_code='#0002')
    data_science_course = Course(course_name='Data Science', course_code='#0003')

    # Student objects
    king: Student = Student(name='King', age=20, student_id='KNG1')
    queen: Student = Student(name='Queen', age=22, student_id='QEN2')
    jack: Student = Student(name='Jack', age=19, student_id='JCK3')

    # Professor objects
    zoro: Professor = Professor(name='Zoro', age=30, professor_id='ZRO1')
    nami: Professor = Professor(name='Nami', age=35, professor_id='NMI2')
    sanji: Professor = Professor(name='Sanji', age=40, professor_id='SNJ3')

    # Department objects
    coding: Department = Department(department_name='Coding')

    # University object
    university: University = University()


    # Assigning Professor objects to Course objects
    python_course.set_professor(professor=zoro)
    ai_course.set_professor(nami)
    sanji.assign_to_course(course=data_science_course)

    # Assigning Student objects to Course objects
    python_course.add_student(student=king)
    python_course.add_student(student=queen)
    jack.enroll(course=python_course)
    king.enroll(course=ai_course)
    ai_course.add_student(jack)
    data_science_course.add_student(queen)

    # Assigning Course objects to Department objects
    coding.add_course(course=python_course)
    coding.add_course(course=ai_course)
    coding.add_course(course=data_science_course)

    # Assigning Professor objects to Department objects
    coding.add_professor(professor=zoro)
    coding.add_professor(professor=nami)
    sanji.setDepartment(department=coding)
    
    # Assigning department objects to University objects
    university.add_department(department=coding)

    # Assigning Student objects to University objects
    university.add_student(student=king)
    university.add_student(student=queen)
    university.add_student(student=jack)

    # Printing University object
    print(university)
    
