'''8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.'''


def make_shirt(size:int, text:str) -> None:
    print(f'The size of the shist is {size} and the text is "{text}".')


#Position arguments
make_shirt(40, "Insane")

#Keyword arguments
make_shirt(text = "T-Shirt", size = 50)