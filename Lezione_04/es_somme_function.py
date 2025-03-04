
#Funzione somma in range a, b
def sumInRange(a:int, b:int):
    sum:int = 0
    for i in range(a, b + 1):
        sum += i
    return sum

#Somma interi da 1 a 10 = 55
somma:int = sumInRange(1, 10)
print(f"La somma tra dei numeri interi tra 1 e 10 compresi è pari a {somma}")
#print(f"Sum from 1 to 10 is {sumInRange(1,10)}")


#Somma interi da 20 a 37 = 513
somma:int = sumInRange(20, 37)
print(f"La somma tra dei numeri interi tra 20 e 37 compresi è pari a {somma}")
#print(f"Sum from 20 to 37 is {sumInRange(20,37)}")

#Somma interi da 35 a 49 = 630
somma:int = sumInRange(35, 49)
print(f"La somma tra dei numeri interi tra 35 e 49 compresi è pari a {somma}")
#print(f"Sum from 35 to 49 is {sumInRange(35,49)}")