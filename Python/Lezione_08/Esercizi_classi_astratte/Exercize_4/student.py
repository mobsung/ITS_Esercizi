'''
Create subclasses Student and Professor that inherit from Person and implement the abstract method.

Class Student:
Additional attributes:

student_id,
courses (list of Course instances).
Additional method:

enroll, to enroll the student in a course.
Class Professor:
Additional attributes:

professor_id,
department (a Department instance), 
courses (list of Course instances)
Additional method:

assign_to_course, to assign the professor to a course.
'''

from person import Person
from course import Course

class Student(Person):

    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses: list[Course] = []

    def get_role(self) -> str:
        return 'Student'
    
    def enroll(self, course: 'Course') -> None:
        if course not in self.courses:
            course.add_student(self)
            self.courses.append(course)
        else:
            print(f'Lo studente {self._name} è già iscritto al corso {course}')
    
    def print_courses(self):
        courses_str = '\n'.join(str(course) for course in self.courses)
        print(courses_str)

    def __str__(self):
        return super().__str__() + f' - Role: {self.get_role()}'

if __name__ == '__main__':

    c1: Course = Course('Course1', '#1')
    s1: Student = Student('King', 20, '@1')

    s1.enroll(c1)

