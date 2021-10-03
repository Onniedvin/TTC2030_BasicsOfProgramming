fname = input("Enter first name: ")
sname = input("Enter last name: ")

for i in range(len(fname)):
    print(fname[:0+1], end="")
print(" ", end="")
print(sname[::-1])