'''
4. Create a class Department:

Attributes:

department_name
courses (list of Course instances)
professors (list of Professor instances)
Methods:

add_course, to add a course to the department.
add_professor, to add a professor to the department.
__str__, method to return a string representation of the department.
'''

from professor import Professor
from course import Course

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
            professor.assign_to_course(self)

    def __str__(self):
        professors_str: str = '\n'.join(str(professor) for professor in self._professors)
        courses_str: str = '\n'.join(str(course) for course in self._courses)
        return f'Department name: {self._department_name}\n--> Professors list in Department: {professors_str}\n--> Courses list in Department: {courses_str}'