def show_info():
    print("I'm utils.info")

def substract(num1, num2):
    return num1 - num2
subs = substract(5, 11)
print("substraction returned ", subs)

def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3
avg = average(5, 11, 8)
print("The average of numbers ", avg)

def calc_consumption():
    return
km = float(input("Enter trip length in km: "))
fuelprice = float(input("Enter fuel price/liter: "))
consumption100 = float(input("Enter liter consumption/100 km: "))

kmconver = km*0.01
consumed = kmconver*consumption100
cost = consumed*fuelprice
print("Fuel consumed: ", "%.2f" % round(consumed, 3), "liter")
print("Cost: ", "%.2f" % round(cost, 3), "€")