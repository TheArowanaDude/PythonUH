num1 = int(input("Please enter the first non-negative integer: "))
num2 = int(input("Please enter the second non-negative integer: "))
num3 = int(input("Please enter the third non-negative integer: "))

if( num1 < num2 ):
    if (num1 < num3):
        if(num2 < num3):
            print(num1, num2, num3)
        else:
            print(num1, num3, num2)

if(num2<num1):
    if(num2 < num3 ):
        if(num3 < num1):
            print(num2,num3,num1)
        else:
            print(num2,num1,num3)

if(num3 < num1):
    if(num3 < num2):
        if(num2 < num1):
            print(num3, num2, num1)
        else:
            print(num3,num1,num2)
