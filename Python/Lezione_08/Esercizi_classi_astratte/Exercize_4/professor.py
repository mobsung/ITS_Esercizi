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
        department.add_professor(self)

    def __str__(self):
        return super().__str__() + f' - ID: {self._professor_id}'
    

if __name__ == '__main__':

    d1: Department = Department()
    p1: Professor = Professor('Prof1', 30, '+1', d1)
    print(p1)