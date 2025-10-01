'''
Nel laboratorio bastano pochi campioni per avviare un esperimento: `head(lines, n)` deve restituire solo le prime `n` righe annotate. Gli appunti si versano in un grimorio chiamato `textio_head.txt`. Se il numero richiesto è positivo, il grimorio viene sfogliato dall’inizio: ogni formula letta, purificata dai segni di fine riga, entra in un alambicco-lista finché non si raggiunge la quantità voluta o finché il testo non finisce.
'''

def head(lines: list[str], n: int) -> list[str]:
    filename = 'textio_head.txt'
    
    with open(file=filename, mode='w', encoding='utf-8') as file:

        for line in lines:
            file.write('\n' + line)

    with open(file=filename, mode='r', encoding='utf-8') as file:

        content = file.read()

        content = content.split()

    result: list[str] = []


    for i in range(len(content)):
        if i == n:
            break
        result.append(content[i])
    
    return result



lines = ['Ciao1', 'Ciao2', 'Ciao3']


print(head(lines, 4))