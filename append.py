num = int(input("How many?"))
names = []
for i in range(num):
    name = input("Enter Name: ")
    names.append(name)
for x in range(num, 0, -1):
    print(names[x-1])
