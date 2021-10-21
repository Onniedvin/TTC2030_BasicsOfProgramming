#6.1
def time():
    return
num = int(input("Enter seconds: "))
hour = num//3600
hour1 = num%3600
Min = hour1//60
sec = hour1%60
print(hour, Min, sec, sep=":")


# 6.2
## fahrenheit to celsius
def fahToCel():
    return
fah = int(input("Enter fahrenheit: "))
cel = float(fah-32)*5/9
print("%.2f" % round(cel),"Celsius")

## celsius to fahrenheit
def celToFah():
    return 
cel = int(input("Enter celsius: "))
fah = (float(cel)*9/5+32)
print("%.2f" % round(fah),"Fahrenheit")


#6.3
def students():
    return
add_student = []
while True:
    user_input = input("Enter student name:")
    if user_input:
        add_student.append(user_input)
    else:
        break
print("Student count:", len(add_student))
print(*add_student, sep=", ")


#6.4
def skijump():
    return
j1 = int(input("Give points from judge 1: "))
j2 = int(input("Give points from judge 2: "))
j3 = int(input("Give points from judge 3: "))
j4 = int(input("Give points from judge 4: "))
j5 = int(input("Give points from judge 5: "))
scores = [j1, j2, j3 ,j4 ,j5]
highest = max(scores)
lowest = min(scores)
total = sum(scores) - highest - lowest
print("Total points are:", total)