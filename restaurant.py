print("Welcome to Restaurant Yummy Food!")
i = float(input("How many many people are in your party?: "))
print("Please type 1 if you would like to order the dish or type 0 if you don't want that dish")
counter = 0
foodcost = 0
while(counter < i):
    soup = float(input("Spicy Beef noodle soup ($2.00): ")) * 2.00
    kabob = float(input("Lamb Kabob ($8.00): ")) * 8.00
    pilau = float(input("Lamb Pilau($9.00): ")) * 9.00
    salad = float(input("Garlic Cucumbers Salad($4.00): ")) * 4.00
    foodcost = float(foodcost + soup + kabob + pilau + salad)
    counter = counter + 1

print("Total Cost of Food Items:", foodcost)
tax = round(foodcost * .08, 2)
print("Taxes(%8.00):",tax)
print("Total Cost with Taxes:", (foodcost + tax))
