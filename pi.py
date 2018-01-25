import random
import math

inside_count = 0
for count in range(0,1000):
    distance=math.hypot(random.random(), random.random())
    if (distance < 0.5):
        inside_count+=1
    count+=1
print(4.0 * inside_count/count)
