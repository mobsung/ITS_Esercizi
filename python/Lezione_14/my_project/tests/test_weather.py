from my_project.weather import *
import pytest


# # passed
# def test_check_weather_1():
#     assert check_weather(21.00) == "hot", 'temperatures greater than 20 degree \
#                                            must be considered as hot'

# def test_check_weather_2():
#     assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree \
#                                               must be considered as average temperature'

# def test_check_weather_3():
#     assert check_weather(5.00) == "cold", 'temperatures below 10 degree \
#                                               must be considered as cold temperature'
    
# def test_check_weather_4():
#     assert check_weather(13.00) == "average", 'temperatures between 10 and 20 degree \
#                                               must be considered as average temperature'
    
# def test_check_weather_5():
#     assert check_weather(30.00) == "hot", 'temperatures greater than 20 degree \
#                                            must be considered as hot'
#     assert check_weather(11.00) == "cold", 'temperatures below 10 degree \
#                                               must be considered as cold temperature'


@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])
def test_check_weather(temperature, expected):
    assert check_weather(temperature) == expected