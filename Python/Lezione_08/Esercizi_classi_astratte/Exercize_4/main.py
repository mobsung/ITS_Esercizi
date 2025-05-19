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
        self.student_id = student_id
        self.courses: list[Course] = []

    def get_role(self) -> str:
        return 'Student'
    
    def enroll(self, course) -> None:
        if course not in self.courses:
            course.add_student(Student)
            self.courses.append(course)
        else:
            print(f'Lo studente {self._name} è già iscritto al corso {course}')
    
    def print_courses(self):
        courses_str = '\n'.join(str(course) for course in self.courses)
        print(courses_str)

    def __str__(self) -> str:
        return f'Name: {self._name} - Age: {self._age}'


class Professor(Person):

    def __init__(self, name: str, age: int, professor_id: str, department):
        super().__init__(name, age)
        self.professor_id = professor_id
        self.courses: list[Course] = []

    def get_role(self) -> str:
        return 'Professor'
    
    def assign_to_course(self, course) -> None:
        pass


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
        return f'Course name: {self._course_name} - Course Code: {self._course_code}'
    
    def print_students(self):
        student_str = '\n'.join(str(student) for student in self._students)
        print(student_str)
    

class Department:

    pass



if __name__ == '__main__':

    c1: Course = Course('Course1', '#1')
    s1: Student = Student('King', 20, '@1')

    c1.add_student(s1)
    #s1.enroll(c1)
    #print(s1)
    s1.print_courses()
    c1.print_students()