number = int(input("Give a number: "))
# == compares something to something
if number == 10:
    print("number is 10")
elif number <10:
    print("number is less than 10")
elif number >= 20:
    print("number is greater than or equal to 20")
else:
    print("number is in between 11 and 19")

number = int(input("give another number: "))
if number > 0 and number < 10:
    print("number is in between 1 and 9")
elif number >= 10 or number == 0:
    print("number is 10 or greater or number is 0")

