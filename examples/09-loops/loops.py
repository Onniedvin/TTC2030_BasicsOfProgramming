number = 10
while number >= 0 and number < 100:
    print(number)
    number -=  1

for i in range(10):
    print("looping range(10): ", i)

for i in range(5, 10):
    print("looping range(5, 10): ", i)

for i in range(0, 10, 2):
    print("looping range(0, 10, 2): ", i)

for character in "blooo":
    print(character)

names = ["Jani", "Joni", "Juni", "Jeni"]
for name in names:
    print(name)

print("running a while loop with break and continue")
number = 0
while True:
    number = int(input("enter a number (0 to exit, 100 ignored): "))
    if number == 0:
        break
    elif number == 100:
        print("ignored")
        continue

    print ("you entered: ", number)
    print("all done, exiting app")
