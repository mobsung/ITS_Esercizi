'''5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!'''



favorite_fruits:list[str] = ["oranges", "watermellons", "bananas"]

if "oranges" in (favorite_fruits):
    print("You really like Oranges!")
if "apples" in (favorite_fruits):
    print("You really like Apples!")
if "lemmons" in (favorite_fruits):
    print("You really like Lemmons!")
if "watermellons" in (favorite_fruits):
    print("You really like Watermellons!")
if "bananas" in (favorite_fruits):
    print("You really like Bananas!")
