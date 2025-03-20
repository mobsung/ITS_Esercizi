'''3. E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
    Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
    Implement a for loop to iterate over the items in the cart and print detailed information about each product and 
    the total.
'''


def product_info(**kwargs) -> dict:
    
    products:dict[str, tuple[float, int]] = {}

    for key, value in kwargs.items():
        products[key] = value
    
    return products


# def shopping_cart():



products = product_info(apples = (2.99, 20), pasta = (3, 5), cola = (5, 10))

print(products)


