'''
9. Caesar Cipher Encryption/Decryption

    Create functions for encrypting and decrypting a message using the Caesar cipher.
    Allow the user to specify the shift value (number of positions to shift each letter).
    Handle both encryption and decryption using the same function with appropriate adjustments.
    Encrypt and decrypt the given message using the specified shift value.

'''

#verify shift value to be a positive Int type 
def is_valid(value) -> bool:
    try:
        if int(value) > 0:  
            return True   
    except ValueError:
        return False


def choose(choice:str = "") -> str:

    while not(choice == "encrypt" or choice == "decrypt"):
        choice = input('Would you like to "encrypt" or "decrypt"?\n==>')

    return choice.lower()


def shiftValue() -> int:

    shift_value:str = input("Choose shift value:\n==>")

    while not is_valid(shift_value):
        shift_value = input("The shift value should be a positive Integer!\nChoose again:\n==>")

    return int(shift_value)


def chooseWord(word:str = "") -> str:

    while not word.isalpha():
        word = input("What word would you like to encrypt/decrypt:\n==>")
        if not word.isalpha():
            word = input("The word isn'd valid,\n >IT SHOULD USE ONLY LETTERS IN THE ALPHABET<\n==>")

    return word.lower()
    

def caesarCipher():
    
    alphabet:str = "abcdefghijklmnopqrstuvwxyz"
    choice:str = choose()
    word:str = chooseWord()
    shift_value: int = shiftValue() % 26

    if choice == "encrypt":
        encrypted_str:str = ""

        for letter in word:
            for index, char in enumerate(alphabet):
                if letter == char:
                    if index + shift_value < len(alphabet):
                        pointer:str = index + shift_value
                    else: 
                        pointer = index + shift_value - len(alphabet)
            
            encrypted_str += alphabet[pointer]
        print(f"The word: {word} - with a shift value of {shift_value} - is Encrypted as: {encrypted_str}")

    if choice == "decrypt":
        decrypted_str:str = ""

        for letter in word:
            for index, char in enumerate(alphabet):
                if letter == char:
                    pointer:str = index - shift_value
    
            decrypted_str += alphabet[pointer]
        print(f"The word: {word} - with a shift value of {shift_value} - is Decrypted as: {decrypted_str}")


caesarCipher()












