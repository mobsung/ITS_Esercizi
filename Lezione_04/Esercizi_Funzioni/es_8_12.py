'''8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.'''



def sandwich_ingrediens(*ingredients:str) -> list:
    print(ingredients)

sandwich_ingrediens("lattuga", "pane", "formaggio")
sandwich_ingrediens("cetriolini", "pane", "maionese")
sandwich_ingrediens("prociutto", "pane", "formaggio")