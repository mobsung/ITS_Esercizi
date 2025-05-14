'''9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
'''



from es_9_4 import Restaurant

if __name__ == "__main__":

    restaurant: Restaurant = Restaurant("Hanami Sushi", "Sushi")
    restaurant.set_number_served()
    restaurant.increment_number_served()
    print(restaurant)