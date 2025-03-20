'''1. School Grading System:

    Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether  
    the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.
'''

from typing import Any
def evaluate_student(name:str, grades:list):

    sum: int = 0
    for index, grade in enumerate(grades):
        sum += int(grade)
        average:float = sum /(index + 1)
    if average >= 60:
        print(f'Student: {name} has passed the exam with an average score of {average}')
    else:
        print(f'Student: {name} has failed the exam with an average score of {average}')


students:list[Any] = [("Marcel", [8, 6, 10]), ("Stefano", [7, 8, 9, 4]), ("Lorenzo", [8, 6, 7])]

for student in students:
    evaluate_student(student[0], student[1])

        