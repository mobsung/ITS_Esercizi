'''6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.'''


from typing import Any
person_data:dict[str, Any] = {"first_name": "Marcel", "last_name": "Movileanu", "Age": 23, "City": "Roma"}
for key, value in person_data.items():
    print(value)