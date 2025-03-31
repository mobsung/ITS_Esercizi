'''5. Inventory Management System:

Create a function that defines an item with a code, name, quantity, and price.
Create a database or dictionary to store the items in inventory.
Implement functions to add, remove, search, and update items in the inventory.
Use for loops and conditional statements to manage the various inventory operations.'''

from typing import Any


def inventory_registrator(inventory:dict[str, dict[str, Any]] = {}, choice = "", code_list: list [Any] = []) -> dict:

    while choice != "finish":
        if choice == "":
            choice = input('Type the "name" of the item that you want to add\n'
                           'Type "finish" if don\'t want to add more items\n==>')
        else:
            if choice != "finish":
                if choice not in inventory:
                    code = input('Type the code of the item!\n==>')
                    while code in code_list:
                        code = input(f'The Code: >#{code}< has already been used!\nChoose a different one!\n==>')
                    if code not in code_list:
                        code_list.append(code)
                    quantity = input('What is the quantity of the item?\n==>')
                    price = input('What is the price of the item?\n==>')
                    
                    inventory[choice] = {"code": f'{code}', "quantity": int(quantity), "price":float(price)}
                else:
                    print(f'The item >{choice}< already exists in the Inventory\n')
            choice = ""
    return inventory


def inventory_manager(inventory: dict = {}):

    choice = ""
    
    while choice != "finish":
        if choice != "finish":

            inventory_info: str = "Inverntory details\n"
            for key, value in inventory.items():
                inventory_info += f'>{key}< - Code: #{value["code"]} - Quantity: {int(value["quantity"])} - Price: {float(value["price"])} $\n'

            choice = input('Type: "add" to add an item to the Inventory"\n'
                           'Type: "remove" to remove an item from the Inventory!\n'
                           'Type: "search" to look at the items in the Inventory!\n'
                           'Type: "update" if you want to modify the >quantity< and the >price< of the items!\n'
                           'Type: "finish" if you are done!\n'
                           '==>'
                          )
            
            if choice == "add":
                item: str = input("What item would you like to add to the list?\n==>")
                if item not in inventory:
                    inventory = inventory_registrator(inventory, item)
                else:
                    print("The Item already exists in the inventory!\n")

            if choice == "remove":
                item: str = input("What item would you like to remove to the list?\n==>")
                
                if item in inventory:
                    inventory.pop(item)
                else:
                    print(f"There aren\'t any >{item}< in the Inventory!\n")
            if choice == "update":
                item: str = input("What item would you like to Update?\n==>")
                if item in inventory:
                    print(f'Current Values of the Item: {item}\n'
                          f'Code: #{inventory[item]["code"]} - '
                          f'Quantity: {inventory[item]["quantity"]} - '
                          f'Price: {inventory[item]["price"]} $\n')
                    
                    parameter: str = input("Chose between >quantity< and >price< to update!\n==>")
                    while not (parameter == "quantity" or parameter == "price"):
                        parameter = input("You have to choose between >quantity< and >price<\n==>")
                    parameter_value: Any = input("What >Value< would you like to set?\n==>")

                    if float(parameter_value) >= 0:
                        inventory[item][parameter] = parameter_value
                    else:
                        while parameter_value < 0:
                            parameter_value: Any = input("The >Value< has to be >= 0!\n==>")
                        inventory[item][parameter] = parameter_value
                else:
                    print(f"There aren\'t any >{item}< in the Inventory!\n")
                                   
            if choice == "search":
                parameter: str = input('Type - "code" if you want to look for the Code of the Item!\n'
                                       'Type - "name" if you want to look for the Name of the Item!\n'
                                       'Type - "all" if you want to look at the whole Inventory!\n==>'
                                      )
                while not (parameter == "code" or parameter == "name" or parameter == "all"):
                        parameter = input("You have to choose between >code< - >name< - >all<\n==>")
                
                if parameter == "code":
                    parameter_value = input("What is the Code you are looking for?\n==>")
                    for key, value in inventory.items():
                        if value["code"] == parameter_value:
                            print(f'The item has been found: >{key}<\n'
                                  f'Code: #{inventory[key]["code"]} - '
                                  f'Quantity: {inventory[key]["quantity"]} - '
                                  f'Price: {inventory[key]["price"]} $\n'
                                  )
                        else:
                            print(f'The code "#{parameter_value}" hasn\'t been found in the inventory')

                if parameter == "name":
                    parameter_value = input("What is the Item you are looking for?\n==>")
                    if parameter_value in inventory:
                        print(f'The item has been found: >{parameter_value}<\n'
                              f'Code: #{inventory[parameter_value]["code"]} - '
                              f'Quantity: {inventory[parameter_value]["quantity"]} - '
                              f'Price: {inventory[parameter_value]["price"]} $\n'
                             )

                if parameter == "all":
                    print(f'{inventory_info}\n')
                

    
inventory_manager()

