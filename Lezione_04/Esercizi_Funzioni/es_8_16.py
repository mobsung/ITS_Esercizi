'''8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *'''



from es_8_14 import car_information
from es_8_14 import car_information as fn
from Esercizi_Funzioni import es_8_14 as mn
from es_8_14 import *


print(car_information('subaru', 'outback', color='blue', tow_package=True))