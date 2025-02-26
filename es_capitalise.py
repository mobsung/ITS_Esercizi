'''Inserita una stringa dall'utente, fornire in output una strina con la prima e l'ultima lettera Maiuscole'''

frase:str = input("Digita una frase:")
frase = frase.title()
words = frase.split(" ")
words_list= []
for word in words:
    p_in = word[:-1]
    p_ultima = word[-1]
    new = p_in + p_ultima.upper()
    words_list.append(new)
print(' '.join(words_list))

