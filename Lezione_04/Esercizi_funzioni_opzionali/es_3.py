'''3. E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
    Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
    Implement a for loop to iterate over the items in the cart and print detailed information about each product and 
    the total.
'''

from typing import Any


def product_info(**kwargs) -> dict:
    
    products:dict[str, list[Any]] = {}

    for key, value in kwargs.items():
        products[key] = value
    
    return products

def shopping_cart(products: dict):

    shopping_list: dict = {}
    choice = ""

    
    while choice != "finish":
        if choice != "finish":

            products_stock: str = "Products in stock\n"
            for product, value in products.items():
                products_stock += f">{product}< - Price: {value[0]}$ - Remaining: {value[1]} pieces\n"

            products_cart: str = "Products in the shopping CART\n"
            for product, value in shopping_list.items():
                total_price :float = ((value[0]*value[1]) / (1 + (value[2] / 100))) * 1.1
                products_cart += f'>{product}< - Total price: {total_price:.2f}$ - Bought: {value[1]} pieces\n'

            choice = input('Type: "add" to add an item to the shopping cart"\n'
                           'Type "remove" to remove an item from the cart!\n'
                           'Type "wiew" to look at the products in the shopping cart and the products in stock!\n'
                           'Type "finish" if you are done!\n'
                           '==>')

            if choice == "add":
                print(products_stock)
                product = input('Type the name of the product you want to "add" to the cart!\n'
                                '==>')
                if products[product][1] > 0:
                    products[product][1] -= 1
                    if product not in shopping_list:
                        shopping_list[product] = [products[product][0], 1, products[product][2]]
                    else:
                        shopping_list[product][1] += 1
                else:
                    print(f'There arent anymore "{product}" in stock!')
                
            if choice == "remove":
                print(products_cart)
                product = input('Type the name of the product you want to "remove" from the cart!\n'
                                '==>')
                if shopping_list[product][1] > 0:
                    products[product][1] += 1
                    if shopping_list[product][1] == 1:
                        shopping_list.pop(product)
                    else:
                        shopping_list[product][1] -= 1
                else:
                    print(f'There arent anymore "{product}" in the shopping list!')

            if choice == "wiew":
                print(products_stock)
                print(products_cart)
        
        

products = product_info(apples = [2.99, 20, 10], pasta = [3, 5, 0], cola = [5, 10, 30], juice = [6, 3, 15], tomatoes = [3.49, 2, 0])
shopping_cart(products)

