#9.1
try:
    list = [1, 2, 3, 4]
    list[5] = 5
except IndexError:
    print("index error")
try:
    list.append(5)
finally:
    print("list correction", list)


#9.2
import os

path = "C:/"
filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        filelist.append(os.path.join(root,file))

for name in filelist:
    print(name)

filename = "ayho.txt"
try:
    file=open("C:\\" + filename, "w")
    file.write("trying to write to drive root, even tough it's not working")
    file.close()
except:
    print("Failed to create file to drive root")
finally:
    import os.path
    path = os.path.expanduser("~/for_jari")
    if not os.path.exists(path): os.makedirs(path)
    path += "/"
    
    file = open(path + filename, "w")
    file.write("DID IT!!")
    file.close

#9.3
def isthiszero(num):
    if num == 0:
        return True
    if isinstance(num, int):
        pass
    if isinstance(num, float):
        pass
    if isinstance(num, str):
        return TypeError("use float or int")
    if num != 0:
        return False
    

num = input("insert number zero ")
try:
    num1 = int(num)
    print(isthiszero(num1))
except ValueError:
    num2 = str(num)
    print(isthiszero((num2)))


#9.4

list2 = [1, 2, 3, 4, 5]
index = int(input("where do you want the text in table? "))
text = input("input text: ")
list2.insert(index, text)
print(list2)