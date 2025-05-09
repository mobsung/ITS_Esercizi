'''
Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')

'''


class FileManager:

    def __init__(self, path:str, mode:str):
        
        self.path = path
        self.mode = mode

    def __enter__(self):

        self.file = open(self.path, self.mode)

        return self.file
    

    def __exit__(self, exc_type, exc_value, traceback):
        
        self.file.close()

        return True


if __name__ == "__main__":

    with FileManager('Python/Lezione_15/Esercizi_context_manager/es_01.txt', 'r') as file1:

        print(file1.read())