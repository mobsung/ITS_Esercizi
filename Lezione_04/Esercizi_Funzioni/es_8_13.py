'''8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"'''



def build_profile(**information) -> dict:
    print(information)

build_profile(firstNome = "Marcel", lastName = "Movileanu", age = "23", hair = "brown", birthDate = "14/03/2001")
