'''6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city's dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.'''


from typing import Any
cities:dict[str, Any] =  {
                          "Rome":{"Country": "Italy", "Population": "2.76 million", "Fact": "Has 280 fountains and more than 900 churches"},
                          "Okinawa":{"Country": "Japan", "Population": "1.47 million", "Fact": "It's 2,271 square km big"},
                          "Hollywood":{"Country": "America", "Population": "70,915", "Fact": "It's the center of the American film industry"}
                          }
for key, value in cities.items():
    for key1, value1 in value.items():
        print(f"{key}: {key1} - {value1}")