def timer(func):

    def wrapper():
        import time
        start: float = time.time()
        func()
        print(time.time() - start)
    return wrapper
