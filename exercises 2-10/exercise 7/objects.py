
from ex7 import Names
adam = Names()
adam.name = "Adam"
adam.age = "18"

eva = Names()
eva.name = "Eva"
eva.age = "18"

print(adam)
print(eva)
print()
print()

from ex7 import Cat
kit = Cat()
kit.name = "Kit"
kit.color = "black"

kat = Cat()
kat.name = "Kat"
kat.color = "white"

print(kit)
print(kat)
kit.meow()
kat.meow()
print()
print()

from ex7 import Car
import random
skoda = Car("Skoda", "Octavia", 3000)
audi = Car("Audi", "A4", 4000)
volvo = Car("Volvo", "V70", 5000)
audi1 = Car("Audi", "m", random.randint(1000, 10000))
bmw = Car("BMW", "m", random.randint(1000, 10000))
ford = Car("Ford", "m", random.randint(1000, 10000))
opel = Car("Opel", "m", random.randint(1000, 10000))
VW = Car("VW", "m", random.randint(1000, 10000))

Vcars = [audi1,bmw,ford,opel,VW]

print("car1:",skoda)
print("car2:",audi)
print("car3:",volvo)
print("Total price of the cars is", skoda.price + audi.price + volvo.price)
print()
print("car4:", audi1)
print("car5:",bmw)
print("car6:",ford)
print("car7:",opel)
print("car8:",VW)
print()

# printing the list
for Vcars in Vcars:
    print(Vcars)