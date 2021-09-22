balance = 2000
print("Bank account balance: ", balance, "€")
euroadd = int(input("How many euros will be added to the balance? "))
centadd = int(input("How many cents will be added to the balance? "))
print("Bank account balance: ", balance + euroadd, end="")
print(".", end="")
print(centadd, "€")