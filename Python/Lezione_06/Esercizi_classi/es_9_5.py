'''9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
'''

class User:


    def __init__(self, first_name: str, last_name: str, age: int, gender: str, login_attempts:int = 0):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts


    def describe_user(self):

        print(f'First name: {self.first_name} - Last name: {self.last_name} - Age: {self.age} - Gender: {self.gender} - Login attempts: {self.login_attempts}')

    
    def increment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):

        self.login_attempts = 0



marcel: User = User("Marcel", "Movileanu", 24, "Male")

marcel.increment_login_attempts()
marcel.increment_login_attempts()
marcel.increment_login_attempts()
marcel.describe_user()
marcel.reset_login_attempts()
marcel.describe_user()
