'''
Password Validation:  Write a function validate_password(password) that checks whether a password meets the following criteria: Minimum length of 20 characters, At least three uppercase letters, At least four special characters (non-alphanumeric). If the password is valid, the function should return True. If the password is invalid, the function should raise a built-in exception (e.g., ValueError) with a message indicating which criteria were not met.
'''

from typing import Any

def validate_password(password: Any):

    upper_char: int = 0
    special_char: int = 0

    for char in password:
        if char.isupper():
            upper_char += 1
        if not char.isalnum():
            special_char += 1

    if upper_char < 3:
        raise ValueError ("The Password should have at least 3 Capital charactrs!")
    if special_char < 4:
        raise ValueError ("The Password should have at least 4 special characters!")
    if len(password) < 20:
        raise ValueError ("The Password should have at least 20 characters!")
    
    return print("Password is Valid")



validate_password("DDDDssss!!!!12345674")