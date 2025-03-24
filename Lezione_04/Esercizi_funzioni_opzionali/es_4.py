'''4. Text Analysis:

Create a function that takes a paragraph and counts the number of occurrences of each word.
The function should print a report showing the most frequent words and their number of occurrences.
You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
Implement error handling to handle missing files or other input issues.
'''


def text_analysis(paragraph: str) -> dict:

    paragraph_list: list[str] = paragraph.split()
    word_dict: dict[str, int] = {}
    
    for word in paragraph_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

def word_counter(word_dict: dict) -> list:

    word_list: list[tuple[str, int]] = []
    
    for word, occurrency in word_dict.items():
        if len(word_list) == 0:
            word_list.append((word, occurrency))
        elif occurrency == word_list[0][1]:
            word_list.append((word, occurrency))
        elif occurrency > word_list[0][1]:
            del word_list[:]
            word_list.append((word, occurrency))
    return word_list


paragraph = '''Create a function that takes a paragraph and counts the number of occurrences of each word.
    The function should print a report showing the most frequent words and their number of occurrences.
    You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
    Implement error handling to handle missing files or other input issues.'''

print(word_counter(text_analysis(paragraph)))
paragraph = paragraph.replace('.', '')
paragraph_list: list[str] = paragraph.split()
print(paragraph_list)


