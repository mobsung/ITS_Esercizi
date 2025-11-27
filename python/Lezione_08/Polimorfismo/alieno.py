

class Alieno():

    '''
    Di un alieno ci interessa sapere la galassia di provenienza
    '''

    def __init__(self, galaxy: str):

        self.setGalaxy(galaxy)


    def setGalaxy(self, galaxy: str) -> None:
        
        if galaxy:
            self.galaxy = galaxy
        else:
            self.galaxy = ""
            print(f'Stringa vuota non valida\n{"-" * 20}')

    
    def getGalaxy(self) -> None:

        return self.galaxy
    

    def __str__(self) -> None:

        return f'Alieno proveniente dalla galassia {self.getGalaxy()}\n{"-" * 20}'
    

    def speak(self) -> None:

        print(f'gfsifgsgou\n{"-" * 20}\n')