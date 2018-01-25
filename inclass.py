guest1 = input("Name of the First Guest: ")
bill1 = float(input("How much did you pay? "))
guest2 = input("Name of 2nd Guest: ")
bill2 = float(input("How much did you pay? "))
print("first guest is",guest1)
print(guest1, "paid", bill1)
print("second guest is", guest2)
print(guest2, "paid", bill2)
total = bill1 + bill2
average_bill = total/2
print("Average bill is", average_bill)
