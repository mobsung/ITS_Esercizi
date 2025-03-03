'''6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.'''


from typing import Any
person_data1:dict[str, Any] = {"first_name": "Marcel", "last_name": "Movileanu", "Age": 23, "City": "Roma"}
person_data2:dict[str, Any] = {"first_name": "Daniela", "last_name": "Movileanu", "Age": 22, "City": "Roma"}
person_data3:dict[str, Any] = {"first_name": "Patrisia", "last_name": "Movileanu", "Age": 24, "City": "Roma"}

people:list[str] = [person_data1, person_data2, person_data3]

for person in people:
    print(person)