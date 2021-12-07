#10.1
lastname = []
while True:
    name = input("give lastname: ")
    lastname.append(name)
    response = input("input \"yes\" to add more names ")
    if response != "yes":
        break
lastname = str(lastname)
filename = "lastnames.txt"
file = open(filename, "w")
file.write(lastname)
file.close


#10.2
count = {}
with open("names.txt") as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in count:
			count[line] += 1
		else:
			count[line] = 1
		line = f.readline()

listitems=list(count.items())
listitems.sort()
print(listitems)


#10.3
def validation(input):
    try:
        value = int(input)
        integer = str(value)
        file = open("int.txt", "w")
        file.write(integer)
    except ValueError:
        try:
            value = float(input)
            Float = str(value)
            file = open("float.txt", "w")
            file.write(Float)
        except ValueError:
            print("input is not a number")


userinput = input("enter an integer or a float: ")
validation(userinput)