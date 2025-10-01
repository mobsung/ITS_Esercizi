'''
Al banco degli esperimenti nessun reagente si usa senza averne annotato la formula in duplice copia: `copy_list(lines)` deve restituire una lista nuova e uguale all’originale. Per questo ogni appunto viene sigillato prima in un grimorio chiamato `textio_source.txt`. Poi, aprendo di nuovo quelle pagine, ogni segno, liberato dalle scorie di fine riga, viene trascritto in un secondo libro, `textio_copy.txt`, e distillato in una lista separata. È questa lista che l’alchimista custodirà come distillato finale.
'''

def copy_list(src: list[str]) -> list[str]:
    source_file = 'textio_source.txt'
    copy_file = 'textio_copy.txt'
    
    
    with open(file=source_file, mode='w', encoding='utf-8') as file:

        for line in src:
            file.write('\n' + line)

    with open(file=source_file, mode='r', encoding='utf-8') as file:

        content = file.read()

        content = content.split()

    with open(file=copy_file, mode='w', encoding='utf-8') as file:

        for line in content:
            file.write('\n' + line)

    with open(file=copy_file, mode='r', encoding='utf-8') as file:

        content_copy = file.read()

        content_copy = content_copy.split()

    return content_copy

    