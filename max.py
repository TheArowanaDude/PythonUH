nums = float(input("Enter as many numbers you like, if you want it to stop, type -1: "))
min = nums
max = nums
while (nums != -1):
    nums = float(input("Enter as many numbers you like, if you want it to stop, type -1: "))
    if(nums > max):
        max = nums
    if(nums < min) and (nums != -1):
        min = nums
print("Your maximum number is", max)
print("Your minimum number is", min)
