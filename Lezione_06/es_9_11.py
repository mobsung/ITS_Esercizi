'''9-11. Imported Admin: Create a module users.py containing three classes:

    User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    Privileges: holds a list of privileges and a method show_privileges() to display them.
    Admin: stores a User instance and a Privileges instance as attributes.

In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.
'''


class User:

    def __init__(self, first_name: str, last_name: str, username: str, email: str):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    
    def describe_user(self):

        print(f'First name: {self.first_name}\nLast name: {self.last_name}\nUsername: {self.username}\nEmail: {self.email}')

    
    def greet_user(self):

        print(f'Hello {self.first_name} {self.last_name}')


class Privileges:

    def __init__(self, privileges: list[str] = []):

        self.privileges = privileges

    
    def set_privileges(self):

        privilege = ""

        while privilege != "finish":
            if privilege == "finish":
                self.privileges.append(input("What are the privileges? (type 'finish' to exit)\n==>"))
            
            privilege = ""
            

    
    def show_privileges(self):

        print(f"Privileges: {', '.join(self.privileges)}")



class Admin:

    def __init__(self, user: User, privileges: Privileges):

        self.user = user
        self.privileges = privileges

    
    def show_info(self):

        self.user.describe_user()
        self.privileges.set_privileges()
        self.privileges.show_privileges()

    

    