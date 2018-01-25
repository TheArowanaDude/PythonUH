import string

k = int(input("Input a number: "))

mainlist = []
intlist = []

for i in range(0,k):
    input_string = input("Input a string")
    mainlist.append(input_string)
for i in mainlist:
    if (i in string.digits):
        intlist.append(int(i))
        mainlist.remove(i)

print(intlist)
print(mainlist)
