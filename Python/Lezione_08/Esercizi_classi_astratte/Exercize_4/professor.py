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
from department import Department


class Professor(Person):

    def __init__(self, name: str, age: int, professor_id: str, department: Department):
        super().__init__(name, age)
        self.professor_id = professor_id
        self.courses: list[Course] = []

    def get_role(self) -> str:
        return 'Professor'
    
    def assign_to_course(self, course: Course) -> None:
        pass