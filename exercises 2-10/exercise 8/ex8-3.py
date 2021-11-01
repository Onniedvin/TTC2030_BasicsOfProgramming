from ex8 import Car
skoda = Car("Skoda", "HFE-123")
audi = Car("Audi", "OFK-523")
volvo = Car("Volvo", "GHI-124")
honda = Car("Honda", "IBN-745")
bmw = Car("BMW", "LOL-345")
ford = Car("Ford", "PQR-189")
opel = Car("Opel", "EXR-146")
ty = Car("Toyota", "KLN-093")
hyundai = Car("Hyundai", "ZAB-865")
am = Car("Aston Martin", "PGK-918")

Vcars = [audi,bmw,ford,opel,ty,volvo,skoda,honda,hyundai,am]
Vcars.sort(key=lambda self:self.brand)
for car in Vcars:
    print(car)

print()

Vcars.sort(key=lambda self:self.reg)
for car in Vcars:
    print(car)