'''14. Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog" '''


def pangram(string: str) -> bool:
    alpha: str = "abcdefghijklmnopqrstuvwxyz"
    
    new_string: str = "" 
    final_string: str = ""
    
#creazione stringa iniziale
    for char in string:
        if char != " ":
            new_string += char
    final_list:list = sorted(set(new_string.lower()))

#Creazione stringa finale
    for elem in final_list:
         final_string += elem
    
    if final_string == alpha:
        return True
    else:
        return False

print(pangram("The quick brown fox jumps over the lazy dog"))






