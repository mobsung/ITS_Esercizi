'''
Creatura con le seguenti proprietà:
- attributi: nome (di tipo stringa, per indicare il nome della creatura)
- metodi: tutti i metodi standard, ovvero __init__, setter, getter e __str__
In particolare:

    il metodo setNome() deve fare un controllo se il nome inserito sia una stringa valida. In caso contrario, impostare il nome della creatura con il valore di "Creatura Generica".

    il metodo __str__ deve mostrare in output: "Creatura: nome creatura"
'''


class Creatura:

    _nome: str

    def __init__(self, nome: str) -> None:
        self.setNome(nome)

    def setNome(self, nome: str) -> None:
        if nome:
            self._nome = nome
        else:
            self._nome = 'Creatura Generica'

    def nome(self) -> str:
        return self._nome
    
    def __str__(self) -> str:
        return f'Creatura: {self.nome()}'