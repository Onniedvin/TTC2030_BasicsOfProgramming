number = int(input("input intefer: "))
number2 = int(input("input another integer: "))
number3 = int(input("one more: "))
if (number >= number2) and (number >= number3):
    largest = number
elif (number2 >= number) and (number2 >= number3):
    largest = number2
else:
    largest = number3
print("max value: ", largest)