'''9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.'''


from es_9_1 import Restaurant


restaurant_sushi: Restaurant = Restaurant("Hanami Sushi", "Sushi")
restaurant_italian: Restaurant = Restaurant("Pizzeria", "Pizza")
restaurant_chinese: Restaurant = Restaurant("China", "Chinese")


restaurant_sushi.describe_restaurant()
restaurant_italian.describe_restaurant()
restaurant_chinese.describe_restaurant()