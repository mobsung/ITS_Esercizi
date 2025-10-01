'''
Tra gli appunti del laboratorio non ogni reagente è disponibile: `contains_line(lines, needle)` deve rivelare se la formula desiderata è già stata trascritta. Prima tutte le note vengono distillate in un grimorio chiamato `textio_contains.txt`. Poi il grimorio viene riaperto e analizzato: ogni formula, liberata dalle scorie di fine riga, è paragonata con il reagente cercato. Se i segni coincidono, l’esperimento può iniziare; se no, resta incompleto.
'''

def contains_line(lines: list[str], needle: str) -> bool:
    filename = 'textio_contains.txt'
    
    with open(file=filename, mode='w', encoding='utf-8') as file:

        for line in lines:
            file.write('\n' + line)

    with open(file=filename, mode='r', encoding='utf-8') as file:

        content = file.read()

        content = content.split()
    
    return True if needle in content else False