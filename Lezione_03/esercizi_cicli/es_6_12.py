'''6-12. Extensions: We're now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.'''



from typing import Any
cities:dict[str, Any] =  {
                          "Rome":{"Country": "Italy", "Population": "2.76 million", "Fact": "Has 280 fountains and more than 900 churches"},
                          "Okinawa":{"Country": "Japan", "Population": "1.47 million", "Fact": "It's 2,271 square km big"},
                          "Hollywood":{"Country": "America", "Population": "70,915", "Fact": "It's the center of the American film industry"}
                          }
for key, value in cities.items():
    for place in value:
        print(f"{key}: Country - {cities[key]['Country']} | Population - {cities[key]['Population']} | Fact - {cities[key]['Fact']}")
        break
        
        
        