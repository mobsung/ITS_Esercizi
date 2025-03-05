'''8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''



def make_shirt(text:str = "I love Python", size:str = "Large") -> None:
    print(f'The size of the shist is {size} and the text is "{text}".')



make_shirt("Insane", "medium")

