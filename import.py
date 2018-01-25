import random
diceThrow = random.randrange(1, 7)

print(diceThrow)


import Math

def radius(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared **.05
    return result

def area(radius):
    b = 3.14159 * radius**2
    return b

def area2(xo, yo, xp, yp)
