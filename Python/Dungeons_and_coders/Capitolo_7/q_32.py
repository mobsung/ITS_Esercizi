'''
Al banco degli esperimenti ogni reagente va registrato e numerato con cura: `count_lines(lines)` deve dire quante formule sono state annotate. Le note vengono distillate nel grimorio `textio_count.txt`. Una volta sigillato e riaperto, ogni linea è un ingrediente contato uno a uno, finché il calcolo rivela l’esatto numero di voci custodite.
'''


def count_lines(lines: list[str]) -> int:
    filename = 'textio_count.txt'
    
    with open(file=filename, mode='w', encoding='utf-8') as file:

        for line in lines:
            file.write('\n' + line)

    with open(file=filename, mode='r', encoding='utf-8') as file:

        content = file.read()

        content = content.split()

    return len(content)