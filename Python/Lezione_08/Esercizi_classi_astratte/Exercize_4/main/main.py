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
            course.add_student(self)
            self._courses.append(course)
        else:
            print(f'Lo studente {self._name} è già iscritto al corso {course}')
    
    def print_courses(self):
        courses_str = '\n'.join(str(course) for course in self._courses)
        print(courses_str)

    def __str__(self):
        return super().__str__() + f' - ID: {self._student_id} - Role: {self.get_role()}'


class Professor(Person):

    def __init__(self, name: str, age: int, professor_id: str, department: 'Department'):
        super().__init__(name, age)
        self._professor_id = professor_id
        self._courses: list[Course] = []
        self.setDepartment(department)

    def get_role(self) -> str:
        return 'Professor'
    
    def assign_to_course(self, course: 'Course') -> None:
        if course not in self._courses:
            course.set_professor(self)
            self._courses.append(course)

    def setDepartment(self, department: 'Department'):
        self._department = department
        #[department.add_professor(self)

    def __str__(self):
        return super().__str__() + f' - ID: {self._professor_id} - {self._department}'


class Course:

    def __init__(self, course_name: str, course_code: str):
        self._course_name = course_name
        self._course_code = course_code
        self._professor: Professor = ''
        self._students: list[Student] = []

    def add_student(self, student: Student) -> None:
        if student not in self._students:
            self._students.append(student)

    def set_professor(self, professor: Professor) -> None:
        self._professor = professor

    def __str__(self):
        student_str = '\n'.join(str(student) for student in self._students)
        return f'Course name: {self._course_name} - Course Code: {self._course_code} - Course instructor: {self._professor}\n--> Student list\n{student_str}'
                  

class Department:

    def __init__(self, department_name: str):
        self._department_name = department_name
        self._courses: list[Course] = []
        self._professors: list[Professor] = []

    def add_course(self, course: Course):
        if course not in self._courses:
            self._courses.append(course)

    def add_professor(self, professor: Professor):
        if professor not in self._professors:
            self._professors.append(professor)
            professor.setDepartment(self)

    def __str__(self):
        professors_str: str = '\n'.join(str(professor) for professor in self._professors)
        courses_str: str = '\n'.join(str(course) for course in self._courses)
        return f'Department name: {self._department_name}\n--> Professors list in Department: {professors_str}\n--> Courses list in Department: {courses_str}'



if __name__ == '__main__':

    c1: Course = Course('Course1', '#1')
    s1: Student = Student('King', 20, '@1')
    s2: Student = Student('Proxy', 22, '@2')

    d1: Department = Department('DEPARTMENT_1')
    p1: Professor = Professor('Prof1', 30, '+1', d1)

    s1.enroll(c1)
    s2.enroll(c1)
    p1.assign_to_course(c1)
    
    #print(p1)

    print(c1)