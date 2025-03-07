'''8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.'''


def city_country(city:str, country:str) -> None:
    print(city, country, sep=', ')


city_country("Rome", "Italy")
city_country("Paris", "France")
city_country("Santiago", "Chile")