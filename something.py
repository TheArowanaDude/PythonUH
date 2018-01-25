max = int(input("How many numbers do you want to input?: "))
num = 0
for i in range(max):
    count = str(i+1)
    temp = int(input("Please enter number" + " " + count + ": "))
    num += temp

average = num / max
print("The average of", max, "numbers entered is:", average)
