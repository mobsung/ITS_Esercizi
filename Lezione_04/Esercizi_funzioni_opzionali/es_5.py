'''5. Inventory Management System:

Create a function that defines an item with a code, name, quantity, and price.
Create a database or dictionary to store the items in inventory.
Implement functions to add, remove, search, and update items in the inventory.
Use for loops and conditional statements to manage the various inventory operations.'''

from typing import Any


def inventory_registrator(inventory:dict[str, dict[str, Any]] = {}, choice = "") -> dict:

    while choice != "finish":
        if choice == "":
            choice = input('Type the "name" of the item that you want to add\n'
                        'Type "finish" if don\'t want to add more items\n'
                        '==>')
        else:
            if choice != "finish":
                code = input('Type "#" and the number of the item!\n'
                            '==>')
                name = input('What is the name of the item?\n'
                            '==>')
                quantity = input('What is the quantity of the item?\n'
                            '==>')
                price = input('What is the price of the item?\n'
                            '==>')
                inventory[choice] = {"code": f'#{code}', "name": name, "quantity": int(quantity), 
                                     "price":float(price)
                                    }
                choice = ""
    return inventory


def inventory_manager(inventory: dict):

    choice = ""
    
    while choice != "finish":
        if choice != "finish":

            inventory_info: str = "Inverntory details\n"
            for key, value in inventory.items():
                inventory_info += f'>{key}< - Code: {value["code"]} - Name: {value["name"]} - Quantity: {int(value["quantity"])} - Price: {float(value["price"])}\n'

            choice = input('Type: "add" to add an item to the Inventory"\n'
                           'Type: "remove" to remove an item from the Inventory!\n'
                           'Type: "search" to look at the items in the Inventory!\n'
                           'Type: "update" if you are done!\n'
                           'Type: "finish" if you are done!\n'
                           '==>'
                          )
            
            if choice == "add":
                item: str = input("What item would you like to add to the list?\n"
                                "==>")
                if item not in inventory:
                    inventory = inventory_registrator(inventory, item)
                else:
                    print("The Item already exists in the inventory!")

            if choice == "remove":
                item: str = input("What item would you like to remove to the list?\n"
                                "==>")
                if item in inventory:
                    inventory.pop(item)
                else:
                    print(f"There aren\'t any >{item}< in the Inventory!")
            if choice == "update":
                item: str = input("What item would you like to Update?\n"
                                  "==>")
                if item in inventory:
                    print(f'Current Values of the Item: {item}\n'
                          f'Code: {inventory[item]["code"]} -'
                          f'Name: {inventory[item]["name"]}'
                          f'Quantity: {inventory[item]["quantity"]}'
                          f'Price: {inventory[item]["price"]}')
                    parameter: str = input("Chose between >quantity< and >price< to update!\n"
                                           "==>")
                    while parameter != "quantity" or parameter != "price":
                        parameter = input("You have to choose between >quantity< and >price<")
                    parameter_value: Any = input("What >Value< would you like to set?\n"
                                                 "==>")
                    if parameter_value >= 0:
                        inventory[item][parameter] = parameter_value
                    else:
                        while parameter_value < 0:
                            parameter_value: Any = input("The >Value< has to be >= 0!\n"
                                                         "==>")
                        inventory[item][parameter] = parameter_value
                else:
                    print(f"There aren\'t any >{item}< in the Inventory!")
                                   
            if choice == "search":
                print(inventory_info)
                

    
inventory_manager(inventory_registrator())





# items = inventory_registrator(pen = {"code": "#1", "name": "pen", "quantity": 1, "price": 3},
#                               book = {"code": "#2", "name": "book", "quantity": 2, "price": 2.6},
#                               pencil = {"code": "#3", "name": "pencil", "quantity": 3, "price": 3.99},
#                               erazer = {"code": "#4", "name": "erazer", "quantity": 4, "price": 4.50},
#                               ruler = {"code": "#5", "name": "ruler", "quantity": 5, "price": 8},
#                               glue = {"code": "#6", "name": "glue", "quantity": 6, "price": 1},
#                              )

