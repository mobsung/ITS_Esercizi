'''
Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1
'''

import time

class Timer:

    def __init__(self):
        
        self.start_time: float = 0.0
        self.end_time: float = 0.0

    
    def __enter__(self):

        self.start_time: float = time.time()

        return self
    

    def __exit__(self, exc_type, exc_value, traceback):

        self.end_time: float = time.time()
        elapsed_time: float = self.end_time - self.start_time

        print(f'Passed time: {elapsed_time:.8f} seconds!')

        if exc_type is not None:
            print(f'Error: {exc_value}')

        return True


if __name__ == "__main__":

    with Timer():

        print('I\'m in the Timer block')