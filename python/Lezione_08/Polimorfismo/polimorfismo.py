from persona import Persona
from alieno import Alieno


# Creazione oggetto di tipo Persona
person: Persona = Persona(name="King", last_name="Proxy", age=99)

# Visualizziamo le informazioni inerenti alla presona
print(person)

# Creazione oggetto di tipo Alieno
alien : Alieno = Alieno(galaxy="King Galaxy")

# Visualizziamo le informzioni della classe Alieno
print(alien)

# Loggetto person invoca il metodo speak()
person.speak()

#L'oggetto aline invoca il metodo speak()
alien.speak()