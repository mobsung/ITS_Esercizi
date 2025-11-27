'''
10. Anagram Checker:

Create a function that checks whether two given strings are anagrams of each other.
Convert both strings to lowercase and remove any non-alphabetic characters.
Sort the characters of each string and compare the sorted strings for equality.
Indicate whether the strings are anagrams or not.
'''


def removeSpecial(strings:list[str]) -> list[str]:
    
    stripped_list:list[str] = []
    fixed_string:str = ""

    for string in strings:
        for char in string:
            fixed_string += char if char.isalpha() else ""
            fixed_string = ''.join(sorted((fixed_string).lower()))
        stripped_list.append(fixed_string)
        fixed_string = ""

    return stripped_list


def getWords(choice:str = "") ->list[str]:

    string_list:list[str] = []
    while choice != "finish" or len(string_list) < 2:

        choice = input('Type "add" if you want to add strings to check for Anagrams\n'
                       'Type "finish if you are done\n==>"')
        
        if choice == "finish" and len(string_list) < 2:
            print("You should add at least 2 string to check for Anagrams\n")

        if choice.lower() == "add":

            string:str = input("What words would you like to check for Anagrams?\n==>")
            string_list.append(string)

    return string_list


def isAnagram():
    string_list:list[str] = getWords()
    stripped_list:list[str] = removeSpecial(string_list)
    test_anagram:bool = True

    for i in range(len(stripped_list)):
        if i == 0:
            test_anagram = test_anagram and stripped_list[i] == stripped_list[i + 1]
        else:
            test_anagram = test_anagram and stripped_list[i] == stripped_list[i - 1]

    if test_anagram == True:
        print(f"The strings: {' <|> '.join(string_list)} \nAre considered anagrams! ✅")
    else:
        print(f"The strings: {' <|> '.join(string_list)} \nAren\'t considered anagrams! ❌")


if __name__ == "__main__":
    isAnagram()