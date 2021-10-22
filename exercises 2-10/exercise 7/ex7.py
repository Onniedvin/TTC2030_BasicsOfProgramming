
# 7.1
class Names:
    def __str__(self):
        return "Name: " + self.name + ", Age: " + self.age

    name = ""
    age = ""


# 7.2
class Cat:
    def __str__(self):
        return self.name + ", Color: " + self.color

    name = ""
    color = ""
    
    def meow(self):
        print(self.name + " says: Meoooooow!")


# 7.3
class Car:
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price)

    brand = ""
    model = ""
    price = 0