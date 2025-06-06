'''9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. '''



class Restaurant:


    def __init__(self, restaurant_name: str, cusine_type:str, number_served: int = 0):


        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = number_served
    
    def __str__(self):

        return f'The restaurant {self.restaurant_name} serves {self.cusine_type} - People served until now: {self.number_served}'

    def describe_restaurant(self):

        print(f'The restaurant {self.restaurant_name} serves {self.cusine_type}')

    
    def open_restaurant(self):

        print("The restaurant is open!")

    
    def set_number_served(self):

        self.number_served = int(input('How many people have been served untill now?\n==>'))

    
    def increment_number_served(self):

        self.number_served += int(input("How many more people have been served today?\n==>"))


if __name__ == "__main__":

    restaurant: Restaurant = Restaurant("Hanami Sushi", "Sushi")
    restaurant.set_number_served()
    restaurant.increment_number_served()
    print(restaurant)
