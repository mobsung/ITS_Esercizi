'''
Sul banco degli esperimenti ogni segnale va fissato e ricontrollato: `write_and_read(lines)` deve restituire la serie completa delle trascrizioni, nell’ordine esatto in cui sono state registrate. Prima tutte le osservazioni si condensano in un grimorio chiamato `textio_write_and_read.txt`. Poi, al momento della rilettura, ogni riga viene distillata senza le impurità di fine riga e versata in una lista nuova, che diventa il distillato finale.
'''

def write_and_read(lines: list[str]) -> list[str]:
    filename = 'textio_write_and_read.txt'
    
    with open(file=filename, mode='w', encoding='utf-8') as file:

        for line in lines:
            file.write('\n' + line)
    
    with open(file=filename, mode='r', encoding='utf-8') as file:

        content = file.read()

        content = content.split()
    
    return content


lines = ['Ciao1', 'Ciao2', 'Ciao3']


print(write_and_read(lines))