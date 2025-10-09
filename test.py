from Python.Utility_python.timer import timer


def decorator(func):

    def wrapper(*args):
        print('Number one')
        func(*args)
        print('Number two')
    return wrapper

# def say_whee():
#     print('Whee')


# say_whee = decorator(say_whee)


# print(say_whee)

@decorator
def say_whee(a,b):
    print(a+b)


say_whee(5, 4)

@timer
def say_whee():
    print('Whee')


say_whee()