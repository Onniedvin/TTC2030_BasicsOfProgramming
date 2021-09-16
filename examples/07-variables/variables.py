number = 5
accountbalance = 420.69
print(number)
print(accountbalance)

number = 55
number2 = number + 2
# value of number2 is now 57
print("Number2 is", number2)

# print("number2 is" + str(number2))

number = number * number2
print("Number2 is", number)

# adds 101 to number value, same as (number = number + 101)
number += 101
print("Number2 is", number)

print("Type of variable number is", type(number))
print("Type of variable accountbalance is", type(accountbalance))


# strings
# initialize a string from text
name = "Onni"
lastname = "Roivas"

# initialize string from another variable
fullname = name

# add strings
fullname = name + " " + lastname
print(fullname)

# use format function
age = 20
fullname = "first name: {}. last name: {}. age: {}".format(name, lastname,age)
print(fullname)

# ^same thing, different way
fullname = "first name: " + name + ". lastname: " + lastname + ". age: " + str(age)
print(fullname)

# access characters in a string
text = "ABC"
a = text[0]
b = text[1]
c = text[2]
print("Second character is " + b)

print("Text length is " + str(len(text)) + " characters.")

# compare strings
text2 = "ABD"
if text == text2:
    print("Texts are identical.")
else:
    print("Texts are different.")


# read text from console
line = input("Enter a line of text: ")
print("You entered: " + line)

# if text is input into line field, will result in error
line = input("Enter a number: ")
number = int(line)
print("Number is ", number)

