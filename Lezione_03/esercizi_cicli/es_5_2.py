'''5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

name:str = "Marcel"
print("Is name == 'Marcel'? I predict True.")
print(name == 'Marcel')
print("Is name != 'Marcel'? I predict False.")
print(name != 'Marcel')


name:str = "Marcel"
print("\nIs name == 'Marcel'? I predict True.")
print(name == 'Marcel')
print("Is name == 'marcel'? I predict False.")
print(name == 'Marcel'.lower)


number:int = 5
print("\nIs number > '4'? I predict True.")
print(number > 4)
print("Is number < '4'? I predict False.")
print(number < 4)


age1:int = 10
age2:int = 15
print("\nIs age1 or age2  > '4'? I predict True.")
print(age1 > 4 or age2 > 4)
print("Is age1 and age2 > '12'? I predict False.")
print(age1 > 12 and age2 > 12)


pizza_list:list[str] = ["Pizza Margherita", "Pizza ai Peperoni", "Pizza Diavola", "Pizza ai Funghi"]
print("\nIs Pizza Margherita in 'pizza_list'? I predict True.")
print("Pizza Margherita" in (pizza_list))
print("Focaccia in 'pizza_list'? I predict False.")
print("Focaccia" in (pizza_list))